#include <stdio.h>
#include <time.h>
int main()
{
    // 获取当前时间
    time_t start_time = time(NULL);
    // 待计算执行时间代码
    for (int i = 0; i < 20000; i++)
    {
        printf("%d\n", i);
    }
    time_t end_time = time(NULL);
    // 计算执行时间
    double execution_time = difftime(end_time, start_time);
    printf("Execution time: %.2f s\n", execution_time);
    return 0;
}
