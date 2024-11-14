# -*- coding: utf-8 -*-#
"""
    @project: Data Structure and algorithm
    @Author：lyj
    @file： MyArray.py
    @date：2024/11/13 14:21
    @Software: PyCharm
    @description: 自定义数据结构-数组(适合于读多写少的场景)
"""


class MyArray:
    def __init__(self, capacity):
        self.array = [None] * capacity
        self.size = 0

    def insert(self, index, element):
        """
        向数组中插入数据
        :param index: 待插入位置索引
        :param element: 待插入元素
        """
        # 判断下标是否合法
        if index < 0 or index > self.size:
            raise Exception("Index out of range")
        if self.size >= len(self.array):
            self.resize()
        # 从index+1下标开始，从右往左逐个右移元素
        for i in range(self.size - 1, index - 1, -1):
            self.array[i + 1] = self.array[i]
        # 在index处插入新元素
        self.array[index] = element
        self.size += 1

    def remove(self, index):
        """
        删除数组中的元素
        :param index: 待删除元素位置索引
        """
        # 判断下标是否合法
        if index < 0 or index >= self.size:
            raise Exception("Index out of range")
        # 从index下标开始，从左往右逐个左移元素
        for i in range(index, self.size):
            self.array[i] = self.array[i + 1]
        self.size -= 1

    def __setitem__(self, index, element):
        """
        直接修改数组元素
        :param index: 待修改元素位置索引
        :param element: 需修改的元素
        """
        if index < 0 or index >= self.size:
            raise Exception("Index out of range")
        self.array[index] = element

    def __getitem__(self, index):
        """
        直接获取数组元素
        :param index: 待获取元素位置索引
        :return: 获取到的元素
        """
        if index < 0 or index >= self.size:
            raise Exception("Index out of range")
        return self.array[index]

    def print(self):
        """
        打印数组中的所有元素
        """
        for i in range(self.size):
            print(self.array[i], end=" ")

    def resize(self):
        """
        按照2倍关系对数组进行扩容
        """
        array_new = [None] * len(self.array) * 2
        # 复制旧数组到新数组
        for i in range(self.size):
            array_new[i] = self.array[i]
        self.array = array_new


if __name__ == '__main__':
    # 自定义数据结构-数组 增删查改
    array = MyArray(3)
    array.insert(0, 1)
    array.insert(0, 2)
    array.insert(0, 3)
    array.insert(0, 4)
    array.insert(1, 5)
    print("before:", end=" ")
    array.print()
    print("")
    print("after:", end=" ")
    array.remove(1)
    array.remove(2)
    array.print()

    print("")
    print(array[0], end=" ")
    array[0] = 1
    print(array[0])

    # 使用Python自带的数组 list 增删查改
    my_list = [0, 2, 3, 4, 5]
    print(my_list[1], end=" ")
    my_list[1] = 6
    print(my_list[1])
    my_list.append(6)
    my_list.insert(0, 8)
    print(my_list)
