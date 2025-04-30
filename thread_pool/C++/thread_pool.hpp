#ifndef THREAD_POOL_HPP
#define THREAD_POOL_HPP

#include <pthread.h>
#include "task_queue.hpp"

class ThreadPool
{
private:
    pthread_mutex_t m_mutex;   // 互斥锁
    pthread_cond_t m_notEmpty; // 条件变量
    pthread_t *m_threadIDs;    // 线程ID数组
    pthread_t m_managerID;     // 管理线程ID
    TaskQueue *m_taskQ;        // 任务队列
    int m_minNum;
    int m_maxNum;
    int m_busyNum;
    int m_aliveNum;
    int m_exitNum;
    bool m_shutdown = false; // 线程池是否关闭

    // 工作线程任务函数
    static void *worker(void *arg);
    // 管理线程任务函数
    static void *manager(void *arg);
    void threadExit();

public:
    ThreadPool(int min, int max);
    ~ThreadPool();

    // 添加任务
    void addTask(Task task);
    // 获取忙线程数量
    int getBusyNum();
    // 获取存活线程数量
    int getAliveNum();
};

#endif