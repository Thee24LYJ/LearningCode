# -*- coding: utf-8 -*-#
"""
    @project: Data Structure and algorithm
    @Author: lyj
    @Email: lyijiang.liu@qq.com
    @file: Questions.py
    @date: 2024/11/23 15:49
    @Software: PyCharm
    @description: 面试中常问算法汇总
"""

# """
# # 链表中是否存在环(链表元素重复与否均可)
# """
#
#
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# def is_cycle(head):
#     """
#     判断链表是否有环
#     :param head: 链表头节点
#     :return: 链表存在环返回True,否则返回False
#     """
#     p1 = head
#     p2 = head
#     while p2 is not None and p2.next is not None:
#         p1 = p1.next
#         p2 = p2.next.next
#         if p1 == p2:
#             return True
#     return False
#
#
# if __name__ == '__main__':
#     head = Node(1)
#     node1 = Node(2)
#     node2 = Node(2)
#     node3 = Node(4)
#     node4 = Node(5)
#     head.next = node1
#     node1.next = node2
#     node2.next = node3
#     node3.next = node4
#     node4.next = node1
#     print(is_cycle(head))


# """
# # 最小栈实现，入栈、出栈和取最小元素的时间复杂度为O(1)
# """
#
# class MinStack:
#     def __init__(self):
#         self.main_stack = []
#         self.min_stack = []
#
#     def push(self, x):
#         self.main_stack.append(x)
#         if len(self.min_stack) == 0 or x <= self.min_stack[len(self.min_stack)-1]:
#             self.min_stack.append(x)
#
#     def pop(self):
#         if self.main_stack[len(self.main_stack)-1] == self.min_stack[len(self.min_stack)-1]:
#             self.min_stack.pop()
#         return self.main_stack.pop()
#
#     def get_min(self):
#         if len(self.min_stack) == 0:
#             return None
#         return self.min_stack[len(self.min_stack)-1]
#
#
# if __name__ == '__main__':
#     my_min_stack = MinStack()
#     my_min_stack.push(5)
#     my_min_stack.push(10)
#     my_min_stack.push(7)
#     my_min_stack.push(3)
#     my_min_stack.push(1)
#     print(my_min_stack.get_min())
#     my_min_stack.pop()
#     my_min_stack.pop()
#     my_min_stack.pop()
#     print(my_min_stack.get_min())


# """
# # 求解最大公约数
# """
#
#
# def gcd(a, b):
#     """
#     最大公约数(结合辗转相除法与更相减损术的优势)
#     :param a: 整数1
#     :param b: 整数2
#     :return: 最大公约数
#     """
#     if a == b:
#         return a
#     # a和b为偶数
#     if (a & 1) == 0 and (b & 1) == 0:
#         return gcd(a >> 1, b >> 1) << 1
#     # a为偶数,b为奇数
#     elif (a & 1) == 0 and (b & 1) != 0:
#         return gcd(a >> 1, b)
#     # a为奇数,b为偶数
#     elif (a & 1) != 0 and (b & 1) == 0:
#         return gcd(a, b >> 1)
#     # a和b为奇数
#     else:
#         max_num = max(a, b)
#         min_num = min(a, b)
#         return gcd(max_num - min_num, min_num)
#
#
# if __name__ == '__main__':
#     a = 10
#     b = 20
#     print(gcd(a, b))

# """
# # 判断一个整数是否是2的整数幂次,时间复杂度为O(1)
# """
#
# def is_power_of_2(n):
#     return n & (n - 1) == 0
#
#
# if __name__ == '__main__':
#     num = 6
#     print(is_power_of_2(num))
#     num = 8
#     print(is_power_of_2(num))

# """
# # 无序数组排序后的最大相邻差
# """
#
#
# class Bucket:
#     def __init__(self):
#         self.min = None
#         self.max = None
#
#
# def get_max_sorted_distance(array=[]):
#     # 获取数组最大值和最小值
#     max_value = array[0]
#     min_value = array[0]
#     for i in range(1, len(array)):
#         if array[i] > max_value:
#             max_value = array[i]
#         if array[i] < min_value:
#             min_value = array[i]
#     d = max_value - min_value
#     if d == 0:
#         return 0
#     bucket_num = len(array)
#     buckets = []
#     for i in range(bucket_num):
#         buckets.append(Bucket())
#     # buckets = [Bucket() for _ in range(bucket_num)] # 该行代码作用于前面三行相同
#     # buckets = [Bucket()]*bucket_num # 存在问题 buckets中所有对象地址相同,均为同一对象
#     # 遍历原数组并将每个元素放到桶中
#     for i in range(0, len(array)):
#         index = int((array[i] - min_value) * (bucket_num - 1) / d)
#         if buckets[index].min is None or buckets[index].min > array[i]:
#             buckets[index].min = array[i]
#         if buckets[index].max is None or buckets[index].max < array[i]:
#             buckets[index].max = array[i]
#     # 遍历桶找到最大差值
#     left_max = buckets[0].max
#     max_distance = 0
#     for i in range(1, len(buckets)):
#         if buckets[i].min is None:
#             continue
#         if buckets[i].min - left_max > max_distance:
#             max_distance = buckets[i].min - left_max
#         left_max = buckets[i].max
#     return max_distance
#
#
# if __name__ == '__main__':
#     my_array = [2, 6, 3, 4, 5, 10, 9]
#     print(get_max_sorted_distance(my_array))

# """
# # 使用栈实现队列
# """
#
# class StackQueue:
#     """
#     使用两个栈模拟队列
#     入队时直接入栈stackIn,出队时若stackOut为空则将stackIn所有元素出栈并放入stackOut再将stackOut出栈模拟出队，若stackOut不空则直接出栈
#     """
#     def __init__(self):
#         self.stackIn = []
#         self.stackOut = []
#
#     def enqueue(self, item):
#         """
#         入队操作
#         :param item: 待入队元素
#         """
#         self.stackIn.append(item)
#
#     def dequeue(self):
#         """
#         出队操作
#         :return:
#         """
#         if len(self.stackOut) == 0:
#             if len(self.stackIn) == 0:
#                 raise Exception("Stack Empty")
#             while len(self.stackIn) > 0:
#                 self.stackOut.append(self.stackIn.pop())
#         return self.stackOut.pop()
#
#
# if __name__ == '__main__':
#     stack_queue = StackQueue()
#     stack_queue.enqueue(5)
#     stack_queue.enqueue(6)
#     stack_queue.enqueue(7)
#     print(stack_queue.dequeue())
#     print(stack_queue.dequeue())
#     stack_queue.enqueue(8)
#     print(stack_queue.dequeue())
#     print(stack_queue.dequeue())

# """
# # 字典序算法(寻找一个整数中所有数字全排列的下一个数)
# """
#
#
# def find_nearest_number(numbers=[]):
#     # 从后往前遍历找到逆序区域前一位(数字置换边界)
#     index = 0
#     for i in range(len(numbers) - 1, 0, -1):
#         if numbers[i] > numbers[i - 1]:
#             index = i
#             break
#     if index == 0:
#         return None
#     # 交换逆序区域前一位和逆序区域中刚好大于它的数字
#     numbers_copy = numbers.copy()
#     head = numbers_copy[index - 1]
#     for i in range(len(numbers_copy) - 1, 0, -1):
#         if head < numbers_copy[i]:
#             numbers_copy[index - 1] = numbers_copy[i]
#             numbers_copy[i] = head
#             break
#     # 将逆序区变为顺序
#     i = index
#     j = len(numbers_copy) - 1
#     while i < j:
#         temp = numbers_copy[i]
#         numbers_copy[i] = numbers_copy[j]
#         numbers_copy[j] = temp
#         i += 1
#         j -= 1
#     return numbers_copy
#
#
# if __name__ == '__main__':
#     my_numbers = [1, 2, 3, 4, 5]
#     for k in range(0, 10):
#         my_numbers = find_nearest_number(my_numbers)
#         for i in my_numbers:
#             print(i, end='')
#         print()

# """
# # 从一个整数中删除k个数字后的最小值 时间/空间复杂度 O(n)
# """
#
#
# def remove_k_digits(num_str, k):
#     new_len = len(num_str) - k
#     if new_len <= 0:
#         return "0"
#     stack = []
#     for i in range(len(num_str)):
#         c = num_str[i]
#         # 若栈顶数字大于当前数字则栈顶数字出栈(删除数字)
#         while len(stack) > 0 and stack[len(stack) - 1] > c and k > 0:
#             stack.pop()
#             k -= 1
#         # 若是数字0且栈空则无需入栈
#         if c == '0' and len(stack) == 0:
#             new_len -= 1
#             if new_len == 0:
#                 return "0"
#             continue
#         stack.append(c)
#     return "".join(stack[:new_len])
#
#
# if __name__ == '__main__':
#     num_str = "541270936"
#     k = 3
#     print(remove_k_digits(num_str, k))

# """
# # 寻找两个有序数组合并后的有序数组中位数
# """
#
#
# def find_median_sorted_arrays(arrA, arrB):
#     m, n = len(arrA), len(arrB)
#     # 若数组A长度更长则交换两数组保证数组A为短数组
#     if m > n:
#         arrA, arrB = arrB, arrA
#         m, n = n, m
#     if n == 0:
#         raise ValueError
#     start, end, half_len = 0, m - 1, (m + n + 1) // 2
#     while start <= end:
#         i = (start + end) // 2
#         j = half_len - i
#         # i偏小需右移
#         if i < m and arrB[j - 1] > arrA[i]:
#             start = i + 1
#         # i偏大需左移
#         elif i > 0 and arrA[i - 1] > arrB[j]:
#             end = i - 1
#         else:
#             if i == 0:  # 数组A均大于数组B
#                 max_of_left = arrB[j - 1]
#             elif j == 0:  # 数组A均小于数组B
#                 max_of_left = arrA[i - 1]
#             else:
#                 max_of_left = max(arrA[i - 1], arrB[j - 1])
#             # 合并后数组长度为奇数
#             if (m + n) % 2 == 1:
#                 return max_of_left
#             if i == m:
#                 min_of_right = arrB[j]
#             elif j == n:
#                 min_of_right = arrA[i]
#             else:
#                 min_of_right = min(arrA[i], arrB[j])
#             # 合并后数组长度为偶数
#             return (max_of_left + min_of_right) / 2.0
#
#
# if __name__ == '__main__':
#     my_arr_A = [3, 5, 6, 7, 8, 12, 20]
#     my_arr_B = [1, 10, 17, 18]
#     print(find_median_sorted_arrays(my_arr_A, my_arr_B))


# """
# # 金矿问题(动态规划)
# """
#
#
# def get_best_gold_recursive(w, n, p=[], g=[]):
#     """
#     金矿问题-动态规划-递归版本 时间复杂度O(2^n)
#     :param w: 工人数量
#     :param n: 可选金矿数量
#     :param p: 某座金矿开采所需工人数量
#     :param g: 某座金矿储量
#     :return: 最优收益
#     """
#     if w == 0 or n == 0:
#         return 0
#     if w < p[n - 1]:
#         return get_best_gold_recursive(w, n - 1, p, g)
#     return max(get_best_gold_recursive(w, n - 1, p, g), get_best_gold_recursive(w - p[n - 1], n - 1, p, g) + g[n - 1])
#
#
# def get_best_gold(w, p=[], g=[]):
#     """
#     金矿问题-动态规划 时间复杂度O(nw)
#     :param w: 工人数量
#     :param p: 某座金矿开采所需工人数量
#     :param g: 某座金矿储量
#     :return: 最优收益
#     """
#     # 动态规划二维表 第几行表示第几座金矿 第几列表示有多少个工人
#     result_table = [[0 for i in range(w + 1)] for j in range(len(g) + 1)]
#     for i in range(1, len(g) + 1):
#         for j in range(1, w + 1):
#             if j < p[i - 1]:
#                 result_table[i][j] = result_table[i - 1][j]
#             else:
#                 result_table[i][j] = max(result_table[i - 1][j], result_table[i - 1][j - p[i - 1]] + g[i - 1])
#     return result_table[len(g)][w]
#
#
# def get_best_gold_v2(w, p=[], g=[]):
#     """
#     金矿问题-动态规划 时间复杂度O(n)
#     :param w: 工人数量
#     :param p: 某座金矿开采所需工人数量
#     :param g: 某座金矿储量
#     :return: 最优收益
#     """
#     # 动态规划表 第几列表示有多少个工人
#     result_table = [0] * (w + 1)
#     for i in range(1, len(g) + 1):
#         for j in range(w, 0, -1):
#             if j >= p[i - 1]:
#                 result_table[j] = max(result_table[j], result_table[j - p[i - 1]] + g[i - 1])
#     return result_table[w]
#
#
# if __name__ == '__main__':
#     w = 10
#     n = 5
#     p = [5, 5, 3, 4, 3]
#     g = [400, 500, 200, 300, 350]
#     print(get_best_gold_recursive(w, n, p, g))
#     print(get_best_gold(w, n, p, g))

"""
# 寻找无序数组中出现奇数次的两个整数,其他整数出现偶数次(数组范围为1到100)
"""


def find_odds_nums(array=[]):
    result = [0, 0]
    # 第一次异或得到两个出现奇数次整数的异或值
    xor_result = 0
    for i in range(len(array)):
        xor_result ^= array[i]
    if xor_result == 0:
        raise ValueError
    # 从右往左寻找第一个出现1的二进制位数
    sep = 1
    while (xor_result & sep) == 0:
        sep <<= 1
    # 将原数组分成两组分别异或得到出现奇数次的两个整数
    for i in range(len(array)):
        if (array[i] & sep) == 0:
            result[0] ^= array[i]
        else:
            result[1] ^= array[i]
    return result


if __name__ == '__main__':
    my_array = [4, 1, 2, 2, 5, 1, 4, 1]
    print(find_odds_nums(my_array))
