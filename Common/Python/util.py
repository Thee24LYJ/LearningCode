# -*- coding: utf-8 -*-#
"""
    @project: Python
    @Author: lyj
    @Email: lyijiang.liu@qq.com
    @file: util.py
    @date: 2025/5/11 15:57
    @Software: PyCharm
    @description: 
"""
import os
import platform


def is_connect_internet(test_ip='8.8.8.8'):
    """
    检查网络是否正常连接
    :param test_ip: 待ping的IP地址
    :return: True表示网络正常连接,False表示未正常连接
    """
    if platform.system().lower().startswith('windows'):
        cmd = u"ping {} -n 1".format(test_ip)
    else:
        cmd = u"ping {} -c 1".format(test_ip)
    status = os.system(cmd)
    return status == 0

if __name__ == '__main__':
    print(is_connect_internet())