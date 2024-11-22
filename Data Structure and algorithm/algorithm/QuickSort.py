# -*- coding: utf-8 -*-#
"""
    @project: Data Structure and algorithm
    @Author：lyj
    @file： QuickSort.py
    @date：2024/11/21 13:59
    @Software: PyCharm
    @description: 快速排序算法实现
"""


def partition_double_side(start, end, array=[]):
    """
    分治并交换元素(默认数组第一个元素为基准)-双边循环法
    :param start: 开始索引
    :param end: 结束索引
    :param array: 待分治数组
    :return: 分治后的基准元素位置
    """
    # 基准元素
    pivot = array[start]
    left = start
    right = end
    while left != right:
        # right指针大于left指针且指向元素大于基准元素则左移,否则准备交换
        while right > left and array[right] > pivot:
            right -= 1
        # left指针小于right指针且指向元素小于基准元素则右移,否则准备交换
        while left < right and array[left] <= pivot:
            left += 1
        # 交换元素
        if left < right:
            p = array[left]
            array[left] = array[right]
            array[right] = p
    array[start] = array[left]
    array[left] = pivot
    return left


def partition_single_side(start, end, array=[]):
    """
    分治并交换元素(默认数组第一个元素为基准)-单边循环法
    :param start: 开始索引
    :param end: 结束索引
    :param array: 待分治数组
    :return: 分治后的基准元素位置
    """
    pivot = array[start]
    mark = start
    for i in range(start + 1, end + 1):
        if array[i] < pivot:
            mark += 1
            p = array[mark]
            array[mark] = array[i]
            array[i] = p
    array[start] = array[mark]
    array[mark] = pivot
    return mark


def quick_sort(start, end, array=[]):
    """
    快速排序-递归
    :param start: 开始索引
    :param end: 结束索引
    :param array: 待排序数组
    :return:
    """
    if start >= end:
        return
    # pivot = partition_double_side(start, end, array)
    pivot = partition_double_side(start, end, array)
    quick_sort(start, pivot - 1, array)
    quick_sort(pivot + 1, end, array)


if __name__ == '__main__':
    my_array = [3, 4, 14, 1, 5, 6, 7, 8, 1, -1, 0, 9, 11]
    quick_sort(0, len(my_array) - 1, my_array)
    print(my_array)
