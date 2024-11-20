#include <stdio.h>
#include <sys/time.h>

int main()
{
    struct timeval start_time, end_time;
    // 获取当前时间
    gettimeofday(&start_time, NULL);
    // 待计算执行时间代码
    for (int i = 0; i < 20000; i++)
    {
        printf("%d\n", i);
    }
    gettimeofday(&end_time, NULL);
    // 计算执行时间
    double execution_time = (end_time.tv_sec - start_time.tv_sec) + (end_time.tv_usec - start_time.tv_usec) / 1000000.0;
    printf("Execution time: %.2f s\n", execution_time);
    return 0;
}
