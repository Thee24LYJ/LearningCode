#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Description: 从C/C++风格注释中提取description说明
支持 // 注释格式，支持单行和多行description
TODO: 待测试是否正常执行
"""

import os
import re
from pathlib import Path


def extract_description_from_cpp_comments(content):
    """
    从C/C++风格的//注释中提取description说明
    支持多行描述的情况
    """
    lines = content.split('\n')
    descriptions = []

    # 匹配 // description: xxx 或 //description: xxx 格式
    pattern = re.compile(r'^\\s*//\\s*description[:\\s]*(.+?)$', re.IGNORECASE)

    for line in lines[:100]:  # 只检查前100行，文件开头注释通常在这里
        stripped = line.strip()

        # 跳过空行
        if not stripped:
            continue

        # 检查是否是//注释
        if stripped.startswith('//'):
            match = pattern.match(stripped)
            if match:
                desc = match.group(1).strip()
                if desc:
                    descriptions.append(desc)
        else:
            # 遇到非注释行，停止检查（通常description在文件开头）
            # 但如果当前行看起来还是注释的一部分，继续检查
            if not stripped.startswith('//') and not stripped.startswith('/*'):
                break

    if descriptions:
        # 合并多个description行（处理多行描述）
        return ' '.join(descriptions)

    return "未找到description"


def get_file_description(file_path):
    """
    读取文件并提取description
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            return extract_description_from_cpp_comments(content)
    except UnicodeDecodeError:
        # 尝试其他编码
        try:
            with open(file_path, 'r', encoding='gbk') as f:
                content = f.read()
                return extract_description_from_cpp_comments(content)
        except Exception as e:
            return f"编码错误: {str(e)}"
    except Exception as e:
        return f"读取错误: {str(e)}"


def generate_markdown_table(tc_dir):
    """
    生成Markdown格式的表格
    """
    results = []

    # 检查目录是否存在
    if not os.path.exists(tc_dir):
        print(f"错误: 目录 '{tc_dir}' 不存在")
        return None

    print(f"正在扫描目录: {tc_dir}")
    print("=" * 70)

    # 遍历所有文件
    for root, dirs, files in os.walk(tc_dir):
        for file in sorted(files):
            # 跳过隐藏文件和系统文件
            if file.startswith('.') or file in ['Thumbs.db', '.DS_Store']:
                continue

            file_path = os.path.join(root, file)

            # 获取相对路径（相对于tc目录）
            rel_path = os.path.relpath(file_path, tc_dir)

            # 提取description
            description = get_file_description(file_path)

            results.append((rel_path, description))

            # 打印进度
            print(f"处理: {rel_path}")

    if not results:
        print("未找到任何文件")
        return None

    # 生成Markdown表格
    markdown = "# 文件Description说明汇总\n\n"
    markdown += f"| {'文件名':<50} | {'Description说明':<40} |\n"
    markdown += f"|{'-' * 52}|{'-' * 42}|\n"

    for filename, description in results:
        # 截断过长的description
        display_desc = description[:40] + '...' if len(description) > 40 else description
        markdown += f"| {filename:<50} | {display_desc:<40} |\n"

    return markdown


def save_to_file(content, filename):
    """
    保存内容到文件
    """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"\n结果已保存到: {filename}")


def main():
    # 配置目录
    tc_dir = "tc"  # 可以修改为实际目录路径

    # 生成Markdown表格
    markdown_table = generate_markdown_table(tc_dir)

    if markdown_table:
        print("\n" + "=" * 70)
        print("生成的Markdown表格:")
        print("=" * 70)
        print(markdown_table)

        # 保存到文件
        output_file = "description_table.md"
        save_to_file(markdown_table, output_file)


if __name__ == "__main__":
    main()

