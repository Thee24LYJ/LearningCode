#include <stdio.h>
#include <time.h>

int main()
{
    // 获取当前时间
    clock_t start_time = clock();
    // 待计算执行时间代码
    for (int i = 0; i < 20000; i++)
    {
        printf("%d\n", i);
    }
    clock_t end_time = clock();
    // 计算执行时间
    double execution_time = (double)(end_time - start_time) / CLOCKS_PER_SEC;
    printf("Execution time: %.2f s\n", execution_time);
    return 0;
}
