# -*- coding: utf-8 -*-#
"""
    @project: Data Structure and algorithm
    @Author：lyj
    @file： MyQueue.py
    @date：2024/11/14 16:33
    @Software: PyCharm
    @description: 自定义数据结构-队列(循环队列)
"""


class MyQueue:
    def __init__(self, capacity):
        self.queue = [None] * capacity
        self.front = 0
        self.rear = 0

    def enqueue(self, e):
        """
        向队列中添加元素
        :param e: 待添加元素
        """
        if (self.rear + 1) % len(self.queue) == self.front:
            raise Exception("queue is full")
        self.queue[self.rear] = e
        self.rear = (self.rear + 1) % len(self.queue)

    def dequeue(self):
        """
        从队列中删除元素
        :return: 删除的元素
        """
        if self.front == self.rear:
            raise Exception("queue is empty")
        dequeue_element = self.queue[self.front]
        self.front = (self.front + 1) % len(self.queue)
        return dequeue_element

    def is_empty(self):
        """
        判断队列是否为空
        :return: 空返回True,否则返回False
        """
        return self.front == self.rear

    def print(self):
        """
        打印队列中的所有元素
        """
        i = self.front
        while i != self.rear:
            print(self.queue[i])
            i = (i + 1) % len(self.queue)


if __name__ == '__main__':
    my_queue = MyQueue(5)
    my_queue.enqueue(1)
    my_queue.enqueue(5)
    my_queue.enqueue(1)
    my_queue.dequeue()
    my_queue.dequeue()
    my_queue.enqueue(3)
    my_queue.print()
