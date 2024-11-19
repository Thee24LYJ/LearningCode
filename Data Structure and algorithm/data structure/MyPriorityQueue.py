# -*- coding: utf-8 -*-#
"""
    @project: Data Structure and algorithm
    @Author：lyj
    @file： MyPriorityQueue.py
    @date：2024/11/19 15:34
    @Software: PyCharm
    @description: 
"""


# def up_adjust(array=[]):
#     """
#     二叉树最小堆调整(节点上浮操作)
#     :param array: 原数组
#     """
#     child_index = len(array) - 1
#     parent_index = (child_index - 1) // 2
#     # temp为插入叶节点值
#     temp = array[child_index]
#     while child_index > 0 and temp < array[parent_index]:
#         array[child_index] = array[parent_index]
#         child_index = parent_index
#         parent_index = (child_index - 1) // 2
#     array[child_index] = temp
#
#
# def down_adjust(parent_index, length, array=[]):
#     """
#     二叉树最小堆调整(节点下沉操作)
#     :param parent_index: 待调整节点下标
#     :param length: 二叉堆数组长度
#     :param array: 原数组
#     """
#     # temp为待调整节点值
#     temp = array[parent_index]
#     child_index = 2 * parent_index + 1
#     while child_index < length:
#         # 若有右孩子且右孩子值小于左孩子的值，则定位为右孩子
#         if child_index + 1 < length and array[child_index + 1] < array[child_index]:
#             child_index += 1
#         # 若父结点小于子结点的值直接跳出
#         if temp <= array[child_index]:
#             break
#         array[parent_index] = array[child_index]
#         parent_index = child_index
#         child_index = 2 * child_index + 1
#     array[parent_index] = temp
#
#
# def build_heap(array=[]):
#     """
#     构建二叉堆
#     :param array: 原数组
#     """
#     for i in range((len(array) - 2) // 2, -1, -1):
#         down_adjust(i, len(array), array)
#
#
# if __name__ == '__main__':
#     print("\n二叉堆建堆")
#     array_list = [1, 3, 2, 6, 5, 7, 8, 9, 10, 0]
#     up_adjust(array_list)
#     print("尾节点上调:", end=" ")
#     print(array_list)
#     array_list = [7, 1, 3, 10, 5, 2, 8, 9, 6]
#     build_heap(array_list)
#     print("节点下调:", end=" ")
#     print(array_list)

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
