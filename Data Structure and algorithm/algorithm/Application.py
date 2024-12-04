# -*- coding: utf-8 -*-#
"""
    @project: Data Structure and algorithm
    @Author: lyj
    @Email: lyijiang.liu@qq.com
    @file: Application.py
    @date: 2024/12/2 14:49
    @Software: PyCharm
    @description: 算法的实际应用
"""
import random
from tkinter import Grid

from sympy.physics.units import amount

# """
# # 位图算法(Bitmap)
# """
#
#
# class MyBitmap:
#     def __init__(self, size):
#         self.words = [0] * (self.get_word_index(size - 1) + 1)
#         self.size = size
#
#     def get_bit(self, bit_index):
#         """
#         判断bit_index位是否为1
#         :param bit_index: 待判断位
#         :return: 若为1则返回True, 否则返回False
#         """
#         if bit_index < 0 or bit_index >= self.size:
#             raise Exception("Index out of range")
#         word_index = self.get_word_index(bit_index)
#         return (self.words[word_index] & (1 << bit_index)) != 0
#
#     def set_bit(self, bit_index):
#         """
#         将bit_index位置为1
#         :param bit_index: 待置为1位
#         """
#         if bit_index < 0 or bit_index >= self.size:
#             raise Exception("Index out of range")
#         word_index = self.get_word_index(bit_index)
#         self.words[word_index] |= (1 << bit_index)
#
#     def get_word_index(self, bit):
#         """
#         获取bit个位在words中的索引(words中一个元素为64位, 若bit为128则需两个元素存储)
#         :param bit: 所在比特位数
#         :return: words列表索引
#         """
#         # 除以2^6即64
#         return bit >> 6
#
#
# if __name__ == '__main__':
#     mybitmap = MyBitmap(128)
#     mybitmap.set_bit(126)
#     mybitmap.set_bit(75)
#     print(mybitmap.get_bit(126))
#     print(mybitmap.get_bit(70))


# """
# # LRU算法(最近最少使用->长期不被使用的数据未来被使用的概率也不大)-内存管理算法
# # 采用哈希链表这种数据结构(类似于双向链表)
# # 非线程安全(需加锁实现线程安全)
# """
#
#
# class Node:
#     def __init__(self, key, value):
#         self.key = key
#         self.value = value
#         self.prev = None
#         self.next = None
#
#
# class LRUCache:
#     def __init__(self, limit):
#         self.limit = limit
#         self.hash = {}
#         self.head = None
#         self.tail = None
#
#     def remove_node(self, node):
#         """
#         删除哈希双向链表中的节点
#         :param node: 待删除节点
#         :return: 待删除节点的键
#         """
#         # 节点唯一则直接删除
#         if node == self.head and node == self.tail:
#             self.head, self.tail = None, None
#         elif node == self.tail:
#             self.tail = self.tail.pre
#             self.tail.next = None
#         elif node == self.head:
#             self.head = self.head.next
#             self.head.pre = None
#         else:
#             # 删除中间节点
#             node.pre.next = node.pre
#             node.next.pre = node.pre
#         return node.key
#
#     def add_node(self, node):
#         """
#         向哈希双向链表尾部添加节点
#         :param node: 待添加节点
#         """
#         if self.tail is not None:
#             self.tail.next = node
#             node.pre = self.tail
#             node.next = None
#         self.tail = node
#         if self.head is None:
#             self.head = node
#
#     def refresh_node(self, node):
#         """
#         更新对应节点位置
#         :param node: 待更新节点
#         :return:
#         """
#         # 若访问节点为尾部节点则无需操作
#         if node == self.head:
#             return
#         # 删除原有节点并放到尾部
#         self.remove_node(node)
#         self.add_node(node)
#
#     def get(self, key):
#         """
#         根据键获取值
#         :param key: 键
#         :return: 对应键的值
#         """
#         node = self.hash.get(key)
#         if node is None:
#             return None
#         self.refresh_node(node)
#         return node.value
#
#     def put(self, key, value):
#         """
#         添加键值对到哈希双向链表中去
#         :param key: 键
#         :param value: 值
#         """
#         node = self.hash.get(key)
#         if node is None:
#             if len(self.hash) >= self.limit:
#                 old_key = self.remove_node(self.head)
#                 self.hash.pop(old_key)
#             node = Node(key, value)
#             self.add_node(node)
#             self.hash[key] = node
#         else:
#             node.value = value
#             self.refresh_node(node)
#
#
# if __name__ == '__main__':
#     mylruCache = LRUCache(5)
#     mylruCache.put("1", "用户1")
#     mylruCache.put("2", "用户2")
#     mylruCache.put("3", "用户3")
#     mylruCache.put("4", "用户4")
#     mylruCache.put("5", "用户5")
#     print(mylruCache.get("2"))
#     mylruCache.put("4", "用户4")
#     mylruCache.put("6", "用户6")
#     print(mylruCache.get("1"))
#     print(mylruCache.get("5"))

# """
# # A星寻路算法
# """
#
#
# class Grid:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.f = 0
#         self.g = 0
#         self.h = 0
#         self.parent = None
#
#     def init_grid(self, parent, end):
#         self.parent = parent
#         if parent is not None:
#             self.g = parent.g + 1
#         else:
#             self.g = 1
#         self.h = abs(self.x - end.x) + abs(self.y - end.y)
#         self.h = self.g + self.h
#
#
# def contain_grid(grids, x, y):
#     for grid in grids:
#         if grid.x == x and grid.y == y:
#             return True
#     return False
#
#
# def is_valid_grid(x, y, open_list=[], close_list=[]):
#     """
#     判断网格节点是否有效
#     :param x: 节点x坐标
#     :param y: 节点y坐标
#     :param open_list: 可以到达的节点列表
#     :param close_list: 已到达的节点列表
#     :return: 网格节点有效返回True
#     """
#     # 是否超过边界
#     if x < 0 or x >= len(MAZE) or y < 0 or y >= len(MAZE[0]):
#         return False
#     # 是否有障碍物
#     if MAZE[x][y] == 1:
#         return False
#     # 是否在open_list中
#     if contain_grid(open_list, x, y):
#         return False
#     # 是否在close_list中
#     if contain_grid(close_list, x, y):
#         return False
#     return True
#
#
# def find_min_grid(open_list=[]):
#     """
#     从可以到达节点列表中寻找最小F值的节点
#     :param open_list: 可以到达的节点列表
#     :return: 寻找最小F值的节点
#     """
#     temp_grid = open_list[0]
#     for grid in open_list:
#         if grid.f < temp_grid.f:
#             temp_grid = grid
#     return temp_grid
#
#
# def find_neighbors(grid, open_list=[], close_list=[]):
#     """
#     从当前节点寻找上下左右的有效节点
#     :param grid: 当前节点
#     :param open_list: 可以到达的节点列表
#     :param close_list: 已到达的节点列表
#     :return: 当前节点四周有效节点列表
#     """
#     grid_list = []
#     if is_valid_grid(grid.x, grid.y - 1, open_list, close_list):
#         grid_list.append(Grid(grid.x, grid.y - 1))
#     if is_valid_grid(grid.x, grid.y + 1, open_list, close_list):
#         grid_list.append(Grid(grid.x, grid.y + 1))
#     if is_valid_grid(grid.x - 1, grid.y, open_list, close_list):
#         grid_list.append(Grid(grid.x - 1, grid.y))
#     if is_valid_grid(grid.x + 1, grid.y, open_list, close_list):
#         grid_list.append(Grid(grid.x + 1, grid.y))
#     return grid_list
#
#
# def a_star_search(start, end):
#     """
#     A星搜索算法
#     :param start: 开始节点
#     :param end: 结束节点
#     :return: 搜索路径, 不可达则返回None
#     """
#     open_list = []
#     close_list = []
#     # 开始结束为相同节点
#     if start.x == end.x and start.y == end.y:
#         return start
#
#     # 将起点加入待访问列表中
#     open_list.append(start)
#     while len(open_list) > 0:
#         # 寻找open_list中F值最小的节点作为当前节点
#         current_grid = find_min_grid(open_list)
#         open_list.remove(current_grid)
#         close_list.append(current_grid)
#         # 找到当前节点的所有不在open_list中的临近节点
#         neighbors = find_neighbors(current_grid, open_list, close_list)
#         for grid in neighbors:
#             if grid not in open_list:
#                 # 标记不在open_list中的临近节点parent，G，H和F值
#                 grid.init_grid(current_grid, end)
#                 open_list.append(grid)
#         # 若终点在open_list中则直接返回终点
#         for grid in open_list:
#             if grid.x == end.x and grid.y == end.y:
#                 return grid
#     # 终点不可达
#     return None
#
#
# MAZE = [
#     [0, 0, 0, 1, 0, 0, 0],
#     [1, 0, 1, 1, 0, 0, 0],
#     [0, 0, 1, 1, 0, 1, 0],
#     [0, 1, 0, 1, 0, 1, 0],
#     [0, 0, 0, 0, 0, 1, 0]
#
# ]
#
# if __name__ == '__main__':
#     start = Grid(0, 0)
#     end = Grid(4, 6)
#     result = a_star_search(start, end)
#     # 回溯迷宫路径
#     path = []
#     while result is not None:
#         path.append(Grid(result.x, result.y))
#         result = result.parent
#     for i in range(len(MAZE)):
#         for j in range(len(MAZE[0])):
#             if contain_grid(path, i, j):
#                 print("*, ", end='')
#             else:
#                 print(str(MAZE[i][j]) + ', ', end='')
#         print()

"""
# 抢红包算法
"""


def divide_red_package(total_amount, total_num):
    """
    抢红包算法(二倍均值法) 每次抢到金额位于[0.01,total_amount/total_num * 2 - 1]
    :param total_amount: 总金额
    :param total_num: 总人数
    :return: 所有红包金额列表
    """
    amount_list = []
    rest_amount = total_amount
    rest_num = total_num
    for i in range(0, total_num - 1):
        amount = random.randint(1, int(rest_amount / rest_num * 2) - 1)
        rest_amount = rest_amount - amount
        rest_num = rest_num - 1
        amount_list.append(amount)
    amount_list.append(rest_amount)
    return amount_list


if __name__ == '__main__':
    my_amount_list = divide_red_package(100, 10)
    for my_amount in my_amount_list:
        print(my_amount)
