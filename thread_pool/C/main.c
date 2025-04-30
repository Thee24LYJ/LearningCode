#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include "thread_pool.h"

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
    ThreadPool *pool = threadPoolCreate(3, 10, queueSize);
    for (int i = 0; i < queueSize; i++)
    {
        int *num = (int *)malloc(sizeof(int));
        *num = i + 100;
        threadPoolAdd(pool, taskFunc, num);
    }

    sleep(30);
    threadPoolDestroy(pool);
    return 0;
}