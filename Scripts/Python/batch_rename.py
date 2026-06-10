#!/usr/bin/env python3
"""
批量文件重命名工具
Safe Batch File Renamer

功能：
- 扫描当前目录中的所有文件
- 查找文件名中包含特定字符串的文件
- 将文件名中的目标字符串替换为新字符串
- 支持预览模式（不实际修改文件）
- 支持交互式确认
- 自动生成操作日志

用法：
    python3 batch_renamer.py                    # 交互模式
    python3 batch_renamer.py --find xxx --replace yyy    # 命令行模式
    python3 batch_renamer.py --find xxx --replace yyy --dry-run  # 预览模式
"""

import os
import sys
import argparse
import logging
from datetime import datetime
from pathlib import Path
from typing import List, Tuple, Dict


# ==================== 配置 ====================

# 日志目录
LOG_DIR = Path(".")
# 排除的文件（不参与重命名）
EXCLUDE_FILES = [__file__, 'batch_renamer.py']


# ==================== 核心函数 ====================

def scan_files(target_str: str) -> List[Path]:
    """
    扫描当前目录，查找文件名包含目标字符串的文件

    参数:
        target_str: 目标搜索字符串

    返回:
        List[Path]: 符合条件的文件路径列表
    """
    current_dir = Path.cwd()
    matching_files = []

    print(f"\n[扫描] 当前目录: {current_dir}")
    print(f"[扫描] 搜索目标: '{target_str}'")
    print("-" * 60)

    for item in current_dir.iterdir():
        # 跳过目录
        if item.is_dir():
            continue

        # 跳过隐藏文件（以.开头）
        if item.name.startswith('.'):
            continue

        # 跳过排除列表中的文件
        if item.name in EXCLUDE_FILES:
            continue

        # 检查文件名是否包含目标字符串
        if target_str in item.name:
            matching_files.append(item)

    return matching_files


def generate_new_name(original_name: str, target_str: str, replacement_str: str) -> str:
    """
    生成新文件名

    参数:
        original_name: 原始文件名
        target_str: 目标搜索字符串
        replacement_str: 替换字符串

    返回:
        str: 替换后的新文件名
    """
    new_name = original_name.replace(target_str, replacement_str)
    return new_name


def check_collision(new_path: Path) -> bool:
    """
    检查新文件名是否与已存在的文件冲突

    参数:
        new_path: 新的文件路径

    返回:
        bool: True表示存在冲突，False表示无冲突
    """
    return new_path.exists()


def rename_file(old_path: Path, new_path: Path) -> Tuple[bool, str]:
    """
    执行文件重命名操作

    参数:
        old_path: 原始文件路径
        new_path: 新文件路径

    返回:
        Tuple[bool, str]: (是否成功, 状态消息)
    """
    try:
        old_path.rename(new_path)
        return True, "成功"
    except PermissionError:
        return False, "权限错误（文件可能被其他程序占用）"
    except OSError as e:
        return False, f"系统错误: {str(e)}"
    except Exception as e:
        return False, f"未知错误: {str(e)}"


def setup_logging() -> logging.Logger:
    """
    设置日志记录器

    返回:
        logging.Logger: 配置好的日志记录器
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = LOG_DIR / f"renamer_log_{timestamp}.log"

    # 创建logger
    logger = logging.getLogger("BatchRenamer")
    logger.setLevel(logging.INFO)

    # 文件处理器
    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setLevel(logging.INFO)

    # 控制台处理器
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # 格式化
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


def display_preview(files: List[Path], target_str: str, replacement_str: str) -> List[Tuple[Path, Path]]:
    """
    显示预览列表

    参数:
        files: 匹配的文件列表
        target_str: 目标搜索字符串
        replacement_str: 替换字符串

    返回:
        List[Tuple[Path, Path]]: (原始路径, 新路径) 的列表
    """
    rename_pairs = []
    collisions = []

    print(f"\n[预览] 找到 {len(files)} 个符合条件的文件:")
    print("=" * 70)

    for i, old_path in enumerate(files, 1):
        new_name = generate_new_name(old_path.name, target_str, replacement_str)
        new_path = old_path.parent / new_name

        # 检查冲突
        has_collision = check_collision(new_path) and new_path != old_path

        if has_collision:
            collisions.append((old_path, new_path))
            print(f"  {i}. {old_path.name} → [冲突!] {new_name} ⚠️")
        else:
            rename_pairs.append((old_path, new_path))
            print(f"  {i}. {old_path.name} → {new_name}")

    print("=" * 70)

    if collisions:
        print(f"\n[警告] 发现 {len(collisions)} 个文件名冲突，将跳过这些文件")

    return rename_pairs


def execute_rename(rename_pairs: List[Tuple[Path, Path]], logger: logging.Logger) -> Dict[str, int]:
    """
    执行重命名操作

    参数:
        rename_pairs: (原始路径, 新路径) 列表
        logger: 日志记录器

    返回:
        Dict[str, int]: 统计信息 {'success': 成功数, 'failed': 失败数, 'skipped': 跳过数}
    """
    stats = {'success': 0, 'failed': 0, 'skipped': 0}

    print(f"\n[执行] 开始重命名 {len(rename_pairs)} 个文件...")
    print("-" * 60)

    for old_path, new_path in rename_pairs:
        success, message = rename_file(old_path, new_path)

        if success:
            logger.info(f"重命名成功: {old_path.name} → {new_path.name}")
            print(f"  ✓ {old_path.name} → {new_path.name}")
            stats['success'] += 1
        else:
            logger.error(f"重命名失败: {old_path.name} - {message}")
            print(f"  ✗ {old_path.name} → {new_path.name} [{message}]")
            stats['failed'] += 1

    return stats


def get_user_confirmation() -> bool:
    """
    获取用户确认

    返回:
        bool: True表示确认执行，False表示取消
    """
    while True:
        user_input = input("\n[确认] 是否执行以上重命名操作? (y/n): ").strip().lower()

        if user_input in ['y', 'yes', '是']:
            return True
        elif user_input in ['n', 'no', '否', 'q', 'quit', '退出']:
            return False
        else:
            print("[提示] 请输入 y(yes) 或 n(no)")


def parse_arguments():
    """
    解析命令行参数

    返回:
        argparse.Namespace: 解析后的参数
    """
    parser = argparse.ArgumentParser(
        description='批量文件重命名工具',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例用法:
  python3 batch_renamer.py                          # 交互模式
  python3 batch_renamer.py --find old --replace new     # 替换old为new
  python3 batch_renamer.py -f xxx -r yyy --dry-run     # 预览模式
  python3 batch_renamer.py -f xxx -r yyy --yes         # 自动确认
        """
    )

    parser.add_argument(
        '-f', '--find',
        type=str,
        help='要查找并替换的目标字符串'
    )

    parser.add_argument(
        '-r', '--replace',
        type=str,
        help='替换后的新字符串'
    )

    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='预览模式：仅显示结果，不实际修改文件'
    )

    parser.add_argument(
        '--yes',
        action='store_true',
        help='自动确认：直接执行，不询问用户'
    )

    parser.add_argument(
        '--include-hidden',
        action='store_true',
        help='包含隐藏文件（以.开头的文件）'
    )

    return parser.parse_args()


def interactive_mode(logger: logging.Logger):
    """
    交互模式：提示用户输入

    参数:
        logger: 日志记录器
    """
    print("\n" + "=" * 60)
    print("           批量文件重命名工具 - 交互模式")
    print("=" * 60)

    # 获取目标字符串
    while True:
        target_str = input("\n请输入要查找的字符串 (xxx): ").strip()
        if target_str:
            break
        print("[错误] 目标字符串不能为空")

    # 获取替换字符串
    replacement_str = input("请输入替换后的字符串 (yyy): ").strip()

    # 执行重命名流程
    run_rename_process(target_str, replacement_str, logger, False)


def run_rename_process(target_str: str, replacement_str: str, logger: logging.Logger, auto_confirm: bool, dry_run: bool = False):
    """
    执行重命名流程

    参数:
        target_str: 目标搜索字符串
        replacement_str: 替换字符串
        logger: 日志记录器
        auto_confirm: 是否自动确认
        dry_run: 是否仅预览不执行
    """
    # 扫描文件
    matching_files = scan_files(target_str)

    if not matching_files:
        print(f"\n[结果] 未找到文件名中包含 '{target_str}' 的文件")
        logger.info(f"扫描完成，未找到匹配文件: {target_str}")
        return

    # 显示预览
    rename_pairs = display_preview(matching_files, target_str, replacement_str)

    if not rename_pairs:
        print("\n[结果] 没有可重命名的文件")
        return

    # 确认执行
    if auto_confirm:
        print("\n[自动确认] 跳过确认步骤，直接执行")
        confirmed = True
    else:
        confirmed = get_user_confirmation()

    if not confirmed:
        print("\n[取消] 操作已取消，没有文件被修改")
        logger.info("用户取消操作")
        return

    # 检查是否为预览模式
    if dry_run:
        print("\n[预览模式] 已跳过实际重命名操作")
        logger.info("预览模式：跳过实际执行")
        return

    # 执行重命名
    stats = execute_rename(rename_pairs, logger)

    # 显示统计
    print("\n" + "=" * 60)
    print(f"[完成] 重命名完成!")
    print(f"       成功: {stats['success']} 个")
    print(f"       失败: {stats['failed']} 个")
    print(f"       跳过: {stats['skipped']} 个")
    print("=" * 60)


def main():
    """主函数"""
    # 解析命令行参数
    args = parse_arguments()

    # 设置日志
    logger = setup_logging()
    logger.info("程序启动")

    try:
        # 判断运行模式
        if args.find is None or args.replace is None:
            # 交互模式
            logger.info("进入交互模式")
            interactive_mode(logger)
        else:
            # 命令行模式
            logger.info(f"命令行模式: find='{args.find}', replace='{args.replace}'")

            if args.find == '':
                print("[错误] 目标字符串不能为空")
                sys.exit(1)

            # 执行重命名流程
            run_rename_process(args.find, args.replace, logger, args.yes, args.dry_run)

            # 干运行模式提示
            if args.dry_run:
                print("\n[干运行] 以上仅为预览，未实际修改任何文件")

    except KeyboardInterrupt:
        print("\n\n[中断] 操作已取消")
        logger.warning("用户中断操作")
        sys.exit(0)
    except Exception as e:
        logger.error(f"程序异常: {str(e)}")
        print(f"\n[错误] 程序发生异常: {str(e)}")
        sys.exit(1)

    logger.info("程序正常退出")


if __name__ == "__main__":
    main()

