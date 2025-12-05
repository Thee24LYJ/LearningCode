# -*- coding: utf-8 -*-#
"""
    @project: Data Structure and algorithm
    @Author：lyj
    @file： CountSort.py
    @date：2024/11/22 14:53
    @Software: PyCharm
    @description: 计数排序算法实现
"""


def count_sort(array=[]):
    """
    计数排序-非稳定排序
    :param array: 待排序数组
    :return: 已排序数组
    """
    # 获取数组最大值
    max_value = array[0]
    for i in range(1, len(array)):
        if array[i] > max_value:
            max_value = array[i]
    # 遍历并填充统计数组
    count_array = [0] * (max_value + 1)
    for i in range(0, len(array)):
        count_array[array[i]] += 1
    # 数组排序
    sorted_array = []
    for i in range(0, len(count_array)):
        for j in range(0, count_array[i]):
            sorted_array.append(i)
    return sorted_array


def count_stable_sort(array=[]):
    """
    计数排序-稳定排序
    :param array: 待排序数组
    :return: 已排序数组
    """
    # 获取数组最大值
    min_value = array[0]
    max_value = array[0]
    for i in range(1, len(array)):
        if array[i] > max_value:
            max_value = array[i]
        if array[i] < min_value:
            min_value = array[i]
    d = max_value - min_value
    # 遍历并填充统计数组
    count_array = [0] * (d + 1)
    for i in range(0, len(array)):
        count_array[array[i] - min_value] += 1
    for i in range(1, len(count_array)):
        count_array[i] += count_array[i - 1]
    # 倒序遍历待排序数组并从统计数组中找到正确位置进行排序
    sorted_array = [0] * len(array)
    for i in range(len(array) - 1, -1, -1):
        sorted_array[count_array[array[i] - min_value] - 1] = array[i]
        count_array[array[i] - min_value] -= 1
    return sorted_array


if __name__ == '__main__':
    my_array = [4, 4, 6, 5, 3, 2, 8, 1, 7, 5, 6, 0, 10, 20]
    # my_array = [95, 94, 91, 98, 99, 90, 91, 92]
    print("基础计数排序:", end='')
    print(count_sort(my_array))
    print("优化计数排序:", end='')
    print(count_stable_sort(my_array))
