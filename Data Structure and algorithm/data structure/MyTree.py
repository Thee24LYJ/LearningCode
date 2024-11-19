# -*- coding: utf-8 -*-#
"""
    @project: Data Structure and algorithm
    @Author：lyj
    @file： MyTree.py
    @date：2024/11/18 15:26
    @Software: PyCharm
    @description: 自定义数据结构-二叉树
"""
import queue


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def create_binary_tree(node_list=[]):
    """
    创建二叉树
    :param node_list: 前序遍历序列
    :return: 创建二叉树根节点
    """
    if node_list is None or len(node_list) == 0:
        return None
    data = node_list.pop(0)
    if data is None:
        return None
    node = TreeNode(data)
    node.left = create_binary_tree(node_list)
    node.right = create_binary_tree(node_list)
    return node


"""
    深度优先搜索: 前序遍历,中序遍历,后续遍历
    广度优先遍历: 层次遍历
"""


def pre_order_traversal(node):
    """
    前序遍历二叉树
    :param node: 待遍历二叉树根节点
    :return:
    """
    if node is None:
        return
    print(node.data, end=" ")
    pre_order_traversal(node.left)
    pre_order_traversal(node.right)


def in_order_traversal(node):
    """
    中序遍历二叉树
    :param node: 待遍历二叉树根节点
    :return:
    """
    if node is None:
        return
    in_order_traversal(node.left)
    print(node.data, end=" ")
    in_order_traversal(node.right)


def post_order_traversal(node):
    """
    后续遍历二叉树
    :param node: 待遍历二叉树根节点
    :return:
    """
    if node is None:
        return
    post_order_traversal(node.left)
    post_order_traversal(node.right)
    print(node.data, end=" ")


def level_order_traversal(node):
    """
    层次遍历二叉树
    :param node: 待遍历二叉树根节点
    """
    myqueue = queue.Queue()
    myqueue.put(node)
    while not myqueue.empty():
        node = myqueue.get()
        print(node.data, end=" ")
        if node.left is not None:
            myqueue.put(node.left)
        if node.right is not None:
            myqueue.put(node.right)


if __name__ == '__main__':
    # 前序遍历序列 None为空节点
    node_list = [3, 2, 9, None, None, 10, None, None, 8, None, 4]
    root = create_binary_tree(node_list)
    print("前序遍历:", end=" ")
    pre_order_traversal(root)
    print("")
    print("中序遍历:", end=" ")
    in_order_traversal(root)
    print("")
    print("后续遍历:", end=" ")
    post_order_traversal(root)
    print("")
    print("层次遍历:", end=" ")
    level_order_traversal(root)
