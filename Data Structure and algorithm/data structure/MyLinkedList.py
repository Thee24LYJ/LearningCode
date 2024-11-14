# -*- coding: utf-8 -*-#
"""
    @project: Data Structure and algorithm
    @Author：lyj
    @file： MyLinkedList.py
    @date：2024/11/13 16:22
    @Software: PyCharm
    @description: 自定义数据结构-链表(适合于写多读少的场景)
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.head = None  # 头节点
        self.tail = None  # 尾节点
        self.size = 0

    def get(self, index):
        """
        获取链表索引为index的节点
        :param index: 待获取链表索引
        :return: 获取到的链表节点
        """
        if index < 0 or index >= self.size:
            raise Exception("Index out of range")
        p = self.head
        for i in range(index):
            p = p.next
        return p

    def set(self, index, value):
        """
        修改链表索引为index的节点数据
        :param index: 待修改节点索引
        :param value: 待修改节点数据
        """
        if index < 0 or index >= self.size:
            raise Exception("Index out of range")
        p = self.head
        for i in range(index):
            p = p.next
        p.data = value

    def insert(self, index, data):
        """
        向链表索引为index的地方插入节点
        :param index: 待插入节点索
        :param data: 待插入节点数据
        """
        if index < 0 or index > self.size:
            raise Exception('Index out of range')
        node = Node(data)
        if self.size == 0:  # 空链表
            self.head = node
            self.tail = node
        elif index == 0:  # 头插
            node.next = self.head
            self.head = node
        elif self.size == index:
            self.tail.next = node
            self.tail = node
        else:  # 中间插入
            prev_node = self.get(index - 1)
            node.next = prev_node.next
            prev_node.next = node
        self.size += 1

    def remove(self, index):
        """
        删除链表索引为index的节点
        :param index: 待删除节点索引
        """
        if index < 0 or index >= self.size:
            raise Exception("Index out of range")
        if index == 0:  # 删除头节点
            self.head = self.head.next
        elif index == self.size - 1:  # 删除尾节点
            prev_node = self.get(index - 1)
            prev_node.next = None
            self.tail = prev_node
        else:
            prev_node = self.get(index - 1)
            next_node = prev_node.next.next
            prev_node.next = next_node
        self.size -= 1

    def print(self):
        """
        打印链表中的所有节点
        """
        p = self.head
        while p:
            print(p.data, end=" ")
            p = p.next


if __name__ == '__main__':
    linked_list = MyLinkedList()
    linked_list.insert(0, 1)
    linked_list.insert(1, 2)
    linked_list.insert(2, 3)
    linked_list.print()
    linked_list.remove(2)
    print("")
    linked_list.print()
    print("")
    print(linked_list.get(0).data)
    linked_list.set(0, 30)
    print(linked_list.get(0).data)
