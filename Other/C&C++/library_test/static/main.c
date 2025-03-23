#include <stdio.h>
#include "head.h"
// 静态库测试
/*
static/$ gcc -c ./src/*.c -I ./include/
static/$ ar rcs libcalc.a *.o
static/$ cp libcalc.a ./test/
static/$ cp ./include/head.h ./test/
static/$ cp main.c ./test/
static/$ cd test/
static/test/$ gcc main.c -o main -L ./ -l calc
static/test/$ ./main
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