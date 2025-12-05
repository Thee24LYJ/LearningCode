# -*- coding: utf-8 -*-#
"""
    @project: Data Structure and algorithm
    @Author: lyj
    @Email: lyijiang.liu@qq.com
    @file: BucketSort.py
    @date: 2024/11/22 16:14
    @Software: PyCharm
    @description: 桶排序算法实现
"""


def bucket_sort(array=[]):
    """
    桶排序-稳定排序
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
    # 初始化桶
    bucket_num = len(array)
    bucket_list = []
    for i in range(0, bucket_num):
        bucket_list.append([])
    # 遍历原数组并将每个元素放到桶中
    for i in range(0, len(array)):
        num = int((array[i] - min_value) * (bucket_num - 1) / d)
        bucket = bucket_list[num]
        bucket.append(array[i])
    # 对每个桶内部元素进行排序
    for i in range(0, len(bucket_list)):
        bucket_list[i].sort()
    # 合并所有桶中已排序元素
    sorted_array = []
    for sub_list in bucket_list:
        for element in sub_list:
            sorted_array.append(element)
    return sorted_array


if __name__ == '__main__':
    my_array = [4.12, 6.4, 0.1, 12, 9.3, 4.6, 10.09, 18]
    print(bucket_sort(my_array))
