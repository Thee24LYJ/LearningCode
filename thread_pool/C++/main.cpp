#include <iostream>
#include <unistd.h>
#include "thread_pool.hpp"

void taskFunc(void *arg)
{
    int num = *(int *)arg;
    printf("Task %lu is running, number = %d\n", pthread_self(), num);
    sleep(1);
}

int main()
{
    int queueSize = 100;
    // 创建线程池
    ThreadPool *pool = new ThreadPool(3, 10);
    for (int i = 0; i < queueSize; i++)
    {
        int *num = new (int);
        *num = i + 100;
        pool->addTask(Task(taskFunc, num));
    }

    sleep(30);
    return 0;
}