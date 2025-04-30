#include "thread_pool.hpp"

#include <iostream>
#include <cstring>
#include <unistd.h>
using namespace std;

const int NUMBER = 2;

ThreadPool::ThreadPool(int min, int max)
{
    // 实例化任务队列
    m_taskQ = new TaskQueue;
    do
    {
        m_minNum = min;
        m_maxNum = max;
        m_busyNum = 0;
        m_aliveNum = min;

        // 根据线程最大上限给线程数组分配内存
        m_threadIDs = new pthread_t[m_maxNum];
        if (m_threadIDs == nullptr)
        {
            cerr << "ThreadPool: threadIDs malloc failed!" << endl;
            break;
        }
        // 初始化
        memset(m_threadIDs, 0, sizeof(pthread_t) * m_maxNum);
        if (pthread_mutex_init(&m_mutex, NULL) != 0 ||
            pthread_cond_init(&m_notEmpty, NULL) != 0)
        {
            cerr << "ThreadPool: mutex or cond init failed!" << endl;
            break;
        }
        // 创建工作线程
        for (int i = 0; i < m_minNum; i++)
        {
            pthread_create(&m_threadIDs[i], NULL, worker, this);
            cout << "创建子线程, ID: " << to_string(m_threadIDs[i]) << endl;
        }
        // 创建管理线程
        pthread_create(&m_managerID, NULL, manager, this);
    } while (0);
}

ThreadPool::~ThreadPool()
{
    // 关闭线程池
    m_shutdown = true;
    // 销毁管理者线程
    pthread_join(m_managerID, NULL);
    // 唤醒所有工作线程
    for (int i = 0; i < m_aliveNum; i++)
    {
        pthread_cond_signal(&m_notEmpty);
    }
    if (m_threadIDs)
    {
        delete[] m_threadIDs;
    }
    if (m_taskQ)
    {
        delete m_taskQ;
    }
    pthread_mutex_destroy(&m_mutex);
    pthread_cond_destroy(&m_notEmpty);
}

void ThreadPool::addTask(Task task)
{
    if (m_shutdown)
    {
        cerr << "ThreadPool: thread pool has been shutdown!" << endl;
        return;
    }
    // 添加任务到任务队列 不需要加锁，任务队列中有锁
    m_taskQ->addTask(task);
    // 唤醒工作的线程
    pthread_cond_signal(&m_notEmpty);
}

int ThreadPool::getAliveNum()
{
    int threadNum = 0;
    pthread_mutex_lock(&m_mutex);
    threadNum = m_aliveNum;
    pthread_mutex_unlock(&m_mutex);
    return threadNum;
}

int ThreadPool::getBusyNum()
{
    int busyNum = 0;
    pthread_mutex_lock(&m_mutex);
    busyNum = m_busyNum;
    pthread_mutex_unlock(&m_mutex);
    return busyNum;
}

// 工作线程任务函数
void *ThreadPool::worker(void *arg)
{
    ThreadPool *pool = static_cast<ThreadPool *>(arg);
    while (true)
    {
        // 访问任务队列 取出任务
        pthread_mutex_lock(&pool->m_mutex);
        // 判断任务队列是否为空
        while (pool->m_taskQ->getTaskCount() == 0 && !pool->m_shutdown)
        {
            cout << "thread " << to_string(pthread_self()) << " waiting..." << endl;
            // 等待条件变量
            pthread_cond_wait(&pool->m_notEmpty, &pool->m_mutex);
            // 判断是否销毁线程
            if (pool->m_exitNum > 0)
            {
                pool->m_exitNum--;
                if (pool->m_aliveNum > pool->m_minNum)
                {
                    pool->m_aliveNum--;
                    pthread_mutex_unlock(&pool->m_mutex);
                    pthread_exit(NULL);
                }
            }
        }
        // 判断是否销毁线程池
        if (pool->m_shutdown)
        {
            pthread_mutex_unlock(&pool->m_mutex);
            pool->threadExit();
        }
        // 取出任务
        Task task = pool->m_taskQ->getTask();
        pool->m_busyNum++;
        pthread_mutex_unlock(&pool->m_mutex);
        pool->m_aliveNum++;
        pthread_mutex_unlock(&pool->m_mutex);
        // 执行任务
        cout << "thread " << to_string(pthread_self()) << " start working..." << endl;
        // 执行任务
        task.function(task.arg);
        delete task.arg;
        task.arg = nullptr;

        // 任务执行完毕，减少忙线程数量
        cout << "thread " << to_string(pthread_self()) << " end working..." << endl;
        pthread_mutex_lock(&pool->m_mutex);
        pool->m_busyNum--;
        pthread_mutex_unlock(&pool->m_mutex);
    }
    return nullptr;
}

// 管理者线程任务函数
void *ThreadPool::manager(void *arg)
{
    ThreadPool *pool = static_cast<ThreadPool *>(arg);
    while (!pool->m_shutdown)
    {
        // 每隔3s检查一次
        sleep(3);
        // 取出线程池任务数和线程数
        pthread_mutex_lock(&pool->m_mutex);
        int queueSize = pool->m_taskQ->getTaskCount();
        int aliveNum = pool->m_aliveNum;
        int busyNum = pool->m_busyNum;
        pthread_mutex_unlock(&pool->m_mutex);

        // 创建线程
        // 当前任务个数>存活的线程数 && 存活的线程数<最大线程个数
        if (queueSize > aliveNum && aliveNum < pool->m_maxNum)
        {
            pthread_mutex_lock(&pool->m_mutex);
            int num = 0;
            for (int i = 0; i < pool->m_maxNum && num < NUMBER && pool->m_aliveNum < pool->m_maxNum; ++i)
            {
                if (pool->m_threadIDs[i] == 0)
                {
                    num++;
                    pthread_create(&pool->m_threadIDs[pool->m_aliveNum], NULL, worker, pool);
                    cout << "创建子线程, ID: " << to_string(pool->m_threadIDs[pool->m_aliveNum]) << endl;
                    pool->m_aliveNum++;
                }
            }
            pthread_mutex_unlock(&pool->m_mutex);
        }

        // 销毁多余线程
        // 忙线程数*2 < 存活线程数 && 存活线程数 > 最小线程数
        if (busyNum * 2 < aliveNum && aliveNum > pool->m_minNum)
        {
            pthread_mutex_lock(&pool->m_mutex);
            pool->m_exitNum = NUMBER;
            pthread_mutex_unlock(&pool->m_mutex);
            for (int i = 0; i < NUMBER; ++i)
            {
                pthread_cond_signal(&pool->m_notEmpty);
            }
        }
    }
    return nullptr;
}

// 线程退出
void ThreadPool::threadExit()
{
    pthread_t tid = pthread_self();
    for (int i = 0; i < m_maxNum; ++i)
    {
        if (m_threadIDs[i] == tid)
        {
            m_threadIDs[i] = 0;
            cout << "threadExit() function: thread "
                 << to_string(pthread_self()) << " exiting..." << endl;
            break;
        }
    }
    pthread_exit(NULL);
}