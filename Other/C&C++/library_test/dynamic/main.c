#include <stdio.h>
#include "head.h"
// 动态库测试
/*
$ gcc ./src/*.c -c -fpic -I ./include/
$ gcc -shared *.o -o libcalc.so
// gcc -fPIC -shared -o libcalc.so ./src/*.c -I ./include/ 执行效果与上面两条命令一样
static/$ cp ./include/head.h ./test/
static/$ cp main.c ./test/
static/$ cd test/
$ gcc main.c -o main -L ./ -l calc
$ ./main
*/
int main()
{
    int a = 20;
    int b = 12;
    printf("a = %d, b = %d\n", a, b);
    printf("a + b = %d\n", add(a, b));
    printf("a - b = %d\n", subtract(a, b));
    printf("a * b = %d\n", multiply(a, b));
    printf("a / b = %f\n", divide(a, b));
    return 0;
}