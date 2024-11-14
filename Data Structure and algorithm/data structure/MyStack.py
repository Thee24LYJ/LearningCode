# -*- coding: utf-8 -*-#
"""
    @project: Data Structure and algorithm
    @Author：lyj
    @file： MyStack.py
    @date：2024/11/14 16:25
    @Software: PyCharm
    @description: 自定义数据结构-栈
    @reference: https://hellowac.github.io/pythonds-zh-cn/c3/s5/
"""


class MyStack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """
        向栈中添加元素
        :param item: 待添加元素
        """
        self.items.append(item)

    def pop(self):
        """
        移除栈顶元素
        """
        self.items.pop()

    def is_empty(self):
        """
        判断栈是否为空
        :return: True为空
        """
        return self.items == []

    def top(self):
        """
        获取栈顶元素
        :return: 栈顶元素
        """
        return self.items[-1]

    def size(self):
        """
        获取栈中元素数量
        :return: 栈中元素的数量
        """
        return len(self.items)


if __name__ == '__main__':
    my_stack = MyStack()
    my_stack.push(1)
    my_stack.push(6)
    my_stack.push(3)
    print(my_stack.top())
    my_stack.pop()
    print(my_stack.top())
    my_stack.pop()
    my_stack.pop()
    print(my_stack.is_empty())
    print(my_stack.size())
