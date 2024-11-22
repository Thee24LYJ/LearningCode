# -*- coding: utf-8 -*-#
"""
    @project: Data Structure and algorithm
    @Author：lyj
    @file： MyPriorityQueue.py
    @date：2024/11/19 15:34
    @Software: PyCharm
    @description: 自定义数据结构-优先队列
"""


# 最大优先队列实现
class MyPriorityQueue:
    def __init__(self):
        self.array = []
        self.size = 0

    def enqueue(self, element):
        """
        向优先队列中插入元素
        :param element: 待插入元素
        """
        self.array.append(element)
        self.size += 1
        self.up_adjust()

    def dequeue(self):
        """
        从优先队列中删除元素
        :return: 删除的元素
        """
        if self.size <= 0:
            raise Exception("Priority Queue is empty")
        head = self.array[0]
        self.array[0] = self.array[self.size - 1]
        self.size -= 1
        self.down_adjust()
        return head

    def up_adjust(self):
        """
        二叉树最大堆调整(节点上浮操作)
        """
        child_index = self.size - 1
        parent_index = (child_index - 1) // 2
        # temp为插入叶节点值
        temp = self.array[child_index]
        while child_index > 0 and temp > self.array[parent_index]:
            self.array[child_index] = self.array[parent_index]
            child_index = parent_index
            parent_index = (parent_index - 1) // 2
        self.array[child_index] = temp

    def down_adjust(self):
        """
        二叉树最大堆调整(节点下沉操作)
        """
        parent_index = 0
        # temp为待调整节点值
        temp = self.array[parent_index]
        child_index = 1
        while child_index < self.size:
            # 若有右孩子且右孩子值小于左孩子的值，则定位为右孩子
            if child_index + 1 < self.size and self.array[child_index + 1] > self.array[child_index]:
                child_index += 1
            # 若父结点小于子结点的值直接跳出
            if temp >= self.array[child_index]:
                break
            self.array[parent_index] = self.array[child_index]
            parent_index = child_index
            child_index = 2 * child_index + 1
        self.array[parent_index] = temp


if __name__ == '__main__':
    my_priority_queue = MyPriorityQueue()
    my_priority_queue.enqueue(3)
    my_priority_queue.enqueue(5)
    my_priority_queue.enqueue(10)
    my_priority_queue.enqueue(2)
    my_priority_queue.enqueue(7)
    print(my_priority_queue.dequeue())
    print(my_priority_queue.dequeue())
