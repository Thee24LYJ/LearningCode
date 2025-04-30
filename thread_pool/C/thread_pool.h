#ifndef THREADPOOL_H
#define THREADPOOL_H

#include <pthread.h>
#include <string.h>

// 任务结构体
typedef struct Task
{
    void (*function)(void *arg);
    void *arg;
} Task;

// 线程池结构体
typedef struct ThreadPool
{
    Task *taskQ; // 任务队列
    int queueCapacity;
    int queueSize;
    int queueFront; // 队首
    int queueRear;  // 队尾

    pthread_t managerID;       // 管理者线程ID
    pthread_t *threadIDs;      // 工作线程ID
    int mixNum;                // 最小工作线程
    int maxNum;                // 最大工作线程
    int busyNum;               // 忙线程个数
    int liveNum;               // 存活线程个数
    int exitNum;               // 销毁线程个数
    pthread_mutex_t mutexPool; // 线程池锁
    pthread_mutex_t mutexBusy; // 忙线程锁
    pthread_cond_t notFull;    // 任务队列是否满
    pthread_cond_t notEmpty;   // 任务队列是否空

    int shutdown; // 是否销毁线程池 销毁为1，不销毁为0
} ThreadPool;

// 创建线程池并初始化
ThreadPool *threadPoolCreate(int min, int max, int queueSize);

// 销毁线程池
int threadPoolDestroy(ThreadPool *pool);

// 添加任务
void threadPoolAdd(ThreadPool *pool, void (*func)(void *arg), void *arg);

// 获取线程池工作线程个数
int threadPoolBusyNum(ThreadPool *pool);

// 获取线程池存活线程个数
int threadPoolAliveNum(ThreadPool *pool);

// 工作线程(消费者线程)任务函数
void *worker(void *arg);
// 管理者线程任务函数
void *manager(void *arg);

// 线程退出函数
void threadExit(ThreadPool *pool);

#endif