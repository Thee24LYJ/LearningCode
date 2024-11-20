# -*- coding: utf-8 -*-#
"""
    @project: Data Structure and algorithm
    @Author：lyj
    @file： BubbleSort.py
    @date：2024/11/20 15:24
    @Software: PyCharm
    @description: 冒泡排序算法实现及优化(鸡尾酒排序)
"""


def bubble_sort(array=[]):
    """
    冒泡排序 基础版
    :param array: 待排序数组
    """
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp


def bubble_sort_optimization_v1(array=[]):
    """
    冒泡排序基础版优化v1 一轮循环中没有元素交换则已有序
    :param array: 待排序数组
    """
    for i in range(len(array) - 1):
        # 判断是否有序标志 若一次循环中没有元素交换则已经有序
        is_sorted = True
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
                is_sorted = False
        if is_sorted:
            break

def bubble_sort_optimization_v2(array=[]):
    """
    冒泡排序基础版优化v2 (1)一轮循环中没有元素交换则已有序 (2)数组有序区判断
    :param array:
    """
    # 最后一次交换位置
    last_exchange_index = 0
    # 无序数组边界 每次只需要比较到这里即可 后续都是有序数组
    sort_border = len(array) - 1
    for i in range(len(array) - 1):
        # 判断是否有序标志 若一次循环中没有元素交换则已经有序
        is_sorted = True
        for j in range(sort_border):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
                is_sorted = False
                last_exchange_index = j
        sort_border = last_exchange_index
        if is_sorted:
            break

def cock_tail_sort(array=[]):
    """
    鸡尾酒排序 基础版
    :param array: 待排序数组
    """
    for i in range(len(array) // 2):
        is_sorted = True
        # 奇数轮 从左向右比较和交换
        for j in range(i,len(array)-i-1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                is_sorted = False
        if is_sorted:
            break
        is_sorted = True
        # 偶数轮 从右向左比较和交换
        for j in range(len(array)-i-1,i,-1):
            if array[j] < array[j-1]:
                temp = array[j]
                array[j] = array[j-1]
                array[j-1] = temp
                is_sorted = False
        if is_sorted:
            break

if __name__ == '__main__':
    my_array = [3, 4, 14, 1, 5, 6, 7, 8, 1, -1, 0, 9, 11]
    print(f"冒泡排序前:{my_array}")
    # bubble_sort(my_array)
    # bubble_sort_optimization_v1(my_array)
    bubble_sort_optimization_v2(my_array)
    # cock_tail_sort(my_array)
    print(f"冒泡排序后:{my_array}")
