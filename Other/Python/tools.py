# -*- coding: utf-8 -*-#
"""
    @project: Python
    @Author：lyj
    @file： tools.py
    @date：2024/11/19 16:28
    @Software: PyCharm
    @description: 一些实用Python脚本
"""

import os
import shutil
from pathlib import Path


def purge_cache(path):
    """
    清除pycharm工程中的__pycache__缓存
    :param path: 工程路径
    """
    # 遍历目录下所有文件
    for file_name in os.listdir(path):
        abs_path = os.path.join(path, file_name)
        if file_name == "__pycache__":
            print(f"rm {abs_path}")
            # 删除 `__pycache__` 目录及其中的所有文件
            shutil.rmtree(abs_path)
        elif os.path.isdir(abs_path):
            # 递归调用
            purge_cache(abs_path)


def convert_file(file_path, file_encoding='gbk'):
    """
    修改文件编码格式
    :param file_path: 待修改文件路径
    :param file_encoding: 待修改文件原始编码,如gbk等
    """
    try:
        content = file_path.read_text(encoding=file_encoding)
        file_path.write_text(content, encoding='utf-8')
        print(f"Converted {file_path}")
    except Exception as e:
        print(f"Failed to convert {file_path}: {e}")


def convert_folder(folder_path, file_type="txt", file_encoding='gbk'):
    """
    批量修改文件编码格式
    :param folder_path: 待修改文件夹路径
    :param file_type: 待修改文件后缀类型
    :param file_encoding: 待修改文件原始编码,如gbk等
    """
    for file_path in Path(folder_path).rglob("*." + file_type):
        convert_file(file_path, file_encoding)


if __name__ == "__main__":
    """
    清除pycharm缓存
    """
    # 当前文件的绝对路径列表，按当前系统类型路径分隔符分隔
    path_list = os.path.dirname(
        os.path.abspath(__file__)
    ).split(os.sep)
    # 取当前文件的上上级目录，可根据需要修改
    root_dir = os.sep.join(path_list[0:-2:])
    # 开始清除
    purge_cache(root_dir)

    """
    文件编码批量处理 gbk->utf-8
    """
    folder_path = r"file_folder"  # 替换为你的文件夹路径
    convert_folder(folder_path,file_type='v')
