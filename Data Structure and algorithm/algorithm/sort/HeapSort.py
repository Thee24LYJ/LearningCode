# -*- coding: utf-8 -*-#
"""
    @project: Data Structure and algorithm
    @Author：lyj
    @file： HeapSort.py
    @date：2024/11/21 14:24
    @Software: PyCharm
    @description: 堆排序算法实现
"""


def up_adjust(array=[]):
    """
    二叉树最小堆调整(节点上浮操作)
    :param array: 原数组
    """
    child_index = len(array) - 1
    parent_index = (child_index - 1) // 2
    # temp为插入叶节点值
    temp = array[child_index]
    while child_index > 0 and temp < array[parent_index]:
        array[child_index] = array[parent_index]
        child_index = parent_index
        parent_index = (child_index - 1) // 2
    array[child_index] = temp


def down_adjust_min_heap(parent_index, length, array=[]):
    """
    二叉树最小堆调整(节点下沉操作)
    :param parent_index: 待调整节点下标
    :param length: 二叉堆数组长度
    :param array: 原数组
    """
    # temp为待调整节点值
    temp = array[parent_index]
    child_index = 2 * parent_index + 1
    while child_index < length:
        # 若有右孩子且右孩子值小于左孩子的值，则定位为右孩子
        if child_index + 1 < length and array[child_index + 1] < array[child_index]:
            child_index += 1
        # 若父结点小于子结点的值直接跳出
        if temp <= array[child_index]:
            break
        array[parent_index] = array[child_index]
        parent_index = child_index
        child_index = 2 * child_index + 1
    array[parent_index] = temp


def down_adjust_max_heap(parent_index, length, array=[]):
    """
    二叉树大堆调整(节点下沉操作)
    :param parent_index: 待调整节点下标
    :param length: 二叉堆数组长度
    :param array: 原数组
    """
    # temp为待调整节点值
    temp = array[parent_index]
    child_index = 2 * parent_index + 1
    while child_index < length:
        # 若有右孩子且右孩子值大于左孩子的值，则定位为右孩子
        if child_index + 1 < length and array[child_index + 1] > array[child_index]:
            child_index += 1
        # 若父结点大于子结点的值直接跳出
        if temp >= array[child_index]:
            break
        array[parent_index] = array[child_index]
        parent_index = child_index
        child_index = 2 * child_index + 1
    array[parent_index] = temp


def build_heap(array=[]):
    """
    构建二叉堆
    :param array: 原数组
    """
    for i in range((len(array) - 2) // 2, -1, -1):
        # down_adjust_min_heap(i, len(array), array)
        down_adjust_max_heap(i, len(array), array)


def heap_sort(array=[]):
    """
    堆排序
    :param array: 待排序数组
    """
    # 构建二叉堆(最大堆)
    build_heap(array)
    # 循环交换集合尾部元素到堆顶并调整形成新的最大堆
    for i in range(len(array) - 1, 0, -1):
        # 交换最后一个元素和第一个元素
        temp = array[i]
        array[i] = array[0]
        array[0] = temp
        # 最小堆调整
        # down_adjust_min_heap(0, i, array)
        # 最大堆调整
        down_adjust_max_heap(0, i, array)


if __name__ == '__main__':
    # print("\n二叉堆建堆")
    # array_list = [1, 3, 2, 6, 5, 7, 8, 9, 10, 0]
    # up_adjust(array_list)
    # print("尾节点上调:", end=" ")
    # print(array_list)
    # array_list = [7, 1, 3, 10, 5, 2, 8, 9, 6]
    # build_heap(array_list)
    # print("节点下调:", end=" ")
    # print(array_list)

    my_array = [3, 4, 14, 1, 5, 6, 7, 8, 1, -1, 0, 9, 11]
    heap_sort(my_array)
    print(my_array)
