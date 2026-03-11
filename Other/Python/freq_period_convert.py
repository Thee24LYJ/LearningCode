#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
时钟频率与周期互相转换工具
Frequency <-> Period Converter

物理公式：
- 周期 T = 1 / f (周期等于频率的倒数)
- 频率 f = 1 / T (频率等于周期的倒数)

支持单位：
- 频率：Hz, kHz, MHz, GHz, THz
- 周期：s, ms, us, ns, ps
"""

import re
import sys


# ==================== 常量定义 ====================

# 频率单位乘数
FREQ_UNITS = {
    '': 1e0,      # Hz (基础单位)
    'hz': 1e0,
    'khz': 1e3,   # 千赫兹
    'mhz': 1e6,   # 兆赫兹
    'ghz': 1e9,   # 吉赫兹
    'thz': 1e12,  # 太赫兹
}

# 时间单位乘数
TIME_UNITS = {
    's': 1e0,     # 秒 (基础单位)
    'ms': 1e-3,   # 毫秒
    'us': 1e-6,   # 微秒
    'ns': 1e-9,   # 纳秒
    'ps': 1e-12,  # 皮秒
}

# 所有单位（用于输入验证）
ALL_UNITS = {**FREQ_UNITS, **TIME_UNITS}

# 单位显示名称（用于输出格式化）
FREQ_UNIT_NAMES = {
    1e0: 'Hz',
    1e3: 'kHz',
    1e6: 'MHz',
    1e9: 'GHz',
    1e12: 'THz',
}

TIME_UNIT_NAMES = {
    1e0: 's',
    1e-3: 'ms',
    1e-6: 'μs',
    1e-9: 'ns',
    1e-12: 'ps',
}


# ==================== 核心函数 ====================

def parse_input_value(input_str):
    """
    解析用户输入，提取数值和单位

    参数:
        input_str: 用户输入的字符串，如 "100 MHz", "2.5GHz", "50ns"

    返回:
        tuple: (base_value, input_type)
        - base_value: 转换到基础单位后的数值 (Hz或秒)
        - input_type: 'frequency' 或 'period'

    错误:
        ValueError: 输入格式无效
    """
    # 去除首尾空白并转为小写
    input_str = input_str.strip().lower()

    # 使用正则表达式分离数值和单位
    # 匹配模式：可选的正负号 + 数字（可能有小数点）+ 可选的单位字母
    pattern = r'^([+-]?\d+\.?\d*)\s*([a-z]*)$'
    match = re.match(pattern, input_str)

    if not match:
        raise ValueError(f"无效的输入格式: '{input_str}'")

    # 提取数值和单位
    value_str = match.group(1)
    unit_str = match.group(2)

    # 转换数值为浮点数
    try:
        value = float(value_str)
    except ValueError:
        raise ValueError(f"无法解析数值: '{value_str}'")

    # 处理没有单位的情况（默认为Hz或秒，取决于上下文）
    if unit_str == '':
        return value, None

    # 查找单位对应的乘数
    multiplier = None
    input_type = None

    # 检查是否是频率单位
    if unit_str in FREQ_UNITS:
        multiplier = FREQ_UNITS[unit_str]
        input_type = 'frequency'
    # 检查是否是时间单位
    elif unit_str in TIME_UNITS:
        multiplier = TIME_UNITS[unit_str]
        input_type = 'period'
    else:
        raise ValueError(f"未知单位: '{unit_str}'。支持的单位: {', '.join(ALL_UNITS.keys())}")

    # 转换为基础单位
    base_value = value * multiplier

    return base_value, input_type


def frequency_to_period(frequency_hz):
    """
    将频率转换为周期

    参数:
        frequency_hz: 频率（Hz）

    返回:
        float: 周期（秒）

    错误:
        ZeroDivisionError: 频率为零
    """
    if frequency_hz == 0:
        raise ZeroDivisionError("频率不能为零（无法计算无限周期）")

    period = 1.0 / frequency_hz
    return period


def period_to_frequency(period_s):
    """
    将周期转换为频率

    参数:
        period_s: 周期（秒）

    返回:
        float: 频率（Hz）

    错误:
        ZeroDivisionError: 周期为零
    """
    if period_s == 0:
        raise ZeroDivisionError("周期为零（无法计算无限频率）")

    frequency = 1.0 / period_s
    return frequency


def format_frequency(hz_value):
    """
    格式化频率输出，自动选择最佳单位

    参数:
        hz_value: 频率（Hz）

    返回:
        str: 格式化后的字符串
    """
    abs_value = abs(hz_value)

    # 选择最佳单位
    if abs_value >= 1e12:
        return f"{hz_value / 1e12:.6f} THz"
    elif abs_value >= 1e9:
        return f"{hz_value / 1e9:.6f} GHz"
    elif abs_value >= 1e6:
        return f"{hz_value / 1e6:.6f} MHz"
    elif abs_value >= 1e3:
        return f"{hz_value / 1e3:.6f} kHz"
    else:
        return f"{hz_value:.6f} Hz"


def format_period(s_value):
    """
    格式化周期输出，自动选择最佳单位

    参数:
        s_value: 周期（秒）

    返回:
        str: 格式化后的字符串
    """
    abs_value = abs(s_value)

    # 选择最佳单位
    if abs_value >= 1e0:
        return f"{s_value:.6f} s"
    elif abs_value >= 1e-3:
        return f"{s_value * 1e3:.6f} ms"
    elif abs_value >= 1e-6:
        return f"{s_value * 1e6:.6f} μs"
    elif abs_value >= 1e-9:
        return f"{s_value * 1e9:.6f} ns"
    else:
        return f"{s_value * 1e12:.6f} ps"


# ==================== 用户界面 ====================

def print_header():
    """打印程序头部信息"""
    print("=" * 60)
    print("       时钟频率与周期互相转换工具")
    print("       Frequency <-> Period Converter")
    print("=" * 60)
    print()


def print_menu():
    """打印主菜单"""
    print("请选择转换模式:")
    print("  [1] 频率 -> 周期 (Frequency → Period)")
    print("  [2] 周期 -> 频率 (Period → Frequency)")
    print("  [3] 退出 (Quit)")
    print()


def get_user_input(mode):
    """
    获取用户输入

    参数:
        mode: 'freq' 或 'period'

    返回:
        float: 转换到基础单位的值
    """
    if mode == 'freq':
        prompt = "请输入频率值 (例如: 100MHz, 2.5GHz, 50kHz): "
    else:
        prompt = "请输入周期值 (例如: 10ns, 100us, 1ms): "

    while True:
        try:
            user_input = input(prompt)

            # 检查退出
            if user_input.lower() in ['q', 'quit', 'exit']:
                return None

            # 解析输入
            base_value, input_type = parse_input_value(user_input)

            # 验证类型匹配
            if mode == 'freq' and input_type == 'period':
                print("[警告] 您输入的是周期值，但选择了频率模式。")
                print("       将尝试将周期作为频率处理...")

            if mode == 'period' and input_type == 'frequency':
                print("[警告] 您输入的是频率值，但选择了周期模式。")
                print("       将尝试将频率作为周期处理...")

            return base_value

        except ValueError as e:
            print(f"[错误] {e}")
            print("请重新输入，或输入 'q' 退出")
            print()


def display_result(value, mode):
    """
    显示转换结果

    参数:
        value: 转换后的值（基础单位）
        mode: 'freq' 或 'period'
    """
    print("-" * 40)

    if mode == 'freq':
        # 频率 -> 周期
        formatted = format_period(value)
        print(f"[结果] 周期 = {formatted}")
        print(f"       (= {value:.12f} 秒)")
    else:
        # 周期 -> 频率
        formatted = format_frequency(value)
        print(f"[结果] 频率 = {formatted}")
        print(f"       (= {value:.12f} Hz)")

    print("-" * 40)
    print()


def main():
    """主函数"""
    print_header()

    while True:
        print_menu()

        try:
            choice = input("请选择 (1/2/3): ").strip()

            if choice == '1':
                # 频率 -> 周期
                print("\n【模式: 频率 → 周期】")
                print("支持的频率单位: Hz, kHz, MHz, GHz, THz")
                print("示例输入: 100MHz, 2.5GHz, 1.5e6")
                print()

                base_value = get_user_input('freq')

                if base_value is None:
                    print("已取消操作")
                    print()
                    continue

                try:
                    result = frequency_to_period(base_value)
                    display_result(result, 'freq')
                except ZeroDivisionError as e:
                    print(f"[错误] {e}")
                    print()

            elif choice == '2':
                # 周期 -> 频率
                print("\n【模式: 周期 → 频率】")
                print("支持的周期单位: s, ms, us, ns, ps")
                print("示例输入: 10ns, 100us, 1ms")
                print()

                base_value = get_user_input('period')

                if base_value is None:
                    print("已取消操作")
                    print()
                    continue

                try:
                    result = period_to_frequency(base_value)
                    display_result(result, 'period')
                except ZeroDivisionError as e:
                    print(f"[错误] {e}")
                    print()

            elif choice in ['3', 'q', 'quit', 'exit']:
                # 退出
                print("\n感谢使用！再见！")
                break

            else:
                print("[错误] 无效选择，请输入 1、2 或 3")
                print()

        except KeyboardInterrupt:
            print("\n\n操作已取消")
            break
        except Exception as e:
            print(f"\n[意外错误] {e}")
            print("请重试")
            print()


# ==================== 独立函数接口 ====================

def convert_frequency_to_period(frequency, unit='Hz'):
    """
    独立的频率转周期函数

    参数:
        frequency: 频率数值
        unit: 频率单位 (默认 'Hz')

    返回:
        dict: {'period': 周期值(秒), 'formatted': 格式化字符串}

    示例:
        >>> convert_frequency_to_period(1000, 'kHz')
        {'period': 0.001, 'formatted': '1.000000 ms'}
    """
    # 构建单位字符串
    unit_str = unit.lower().strip()

    if unit_str not in FREQ_UNITS:
        raise ValueError(f"不支持的频率单位: {unit}")

    # 转换为Hz
    freq_hz = frequency * FREQ_UNITS[unit_str]

    # 计算周期
    period_s = frequency_to_period(freq_hz)

    return {
        'period': period_s,
        'formatted': format_period(period_s)
    }


def convert_period_to_frequency(period, unit='s'):
    """
    独立的周期转频率函数

    参数:
        period: 周期数值
        unit: 周期单位 (默认 's')

    返回:
        dict: {'frequency': 频率值(Hz), 'formatted': 格式化字符串}

    示例:
        >>> convert_period_to_frequency(1, 'ms')
        {'frequency': 1000.0, 'formatted': '1.000000 kHz'}
    """
    # 构建单位字符串
    unit_str = unit.lower().strip()

    if unit_str not in TIME_UNITS:
        raise ValueError(f"不支持的周期单位: {unit}")

    # 转换为秒
    period_s = period * TIME_UNITS[unit_str]

    # 计算频率
    freq_hz = period_to_frequency(period_s)

    return {
        'frequency': freq_hz,
        'formatted': format_frequency(freq_hz)
    }


# ==================== 测试代码 ====================

def run_tests():
    """运行测试用例"""
    print("\n" + "=" * 60)
    print("运行测试用例...")
    print("=" * 60 + "\n")

    test_cases = [
        # (输入值, 单位, 模式, 预期结果描述)
        (1000, 'Hz', 'period', '1 ms'),
        (1, 'kHz', 'period', '1 ms'),
        (1, 'MHz', 'period', '1 μs'),
        (2.4, 'GHz', 'period', '≈416.67 ps'),
        (1, 's', 'freq', '1 Hz'),
        (1, 'ms', 'freq', '1 kHz'),
        (1, 'us', 'freq', '1 MHz'),
        (1, 'ns', 'freq', '1 GHz'),
    ]

    print("测试 1: 频率 → 周期")
    print("-" * 40)
    for freq, unit, mode, expected in test_cases[:4]:
        if mode == 'period':
            result = convert_frequency_to_period(freq, unit)
            print(f"  {freq} {unit} → {result['formatted']} (预期: {expected})")

    print("\n测试 2: 周期 → 频率")
    print("-" * 40)
    for period, unit, mode, expected in test_cases[4:]:
        if mode == 'freq':
            result = convert_period_to_frequency(period, unit)
            print(f"  {period} {unit} → {result['formatted']} (预期: {expected})")

    print("\n测试 3: 错误处理")
    print("-" * 40)

    # 测试零值处理
    try:
        convert_frequency_to_period(0, 'Hz')
        print("  [失败] 应该抛出 ZeroDivisionError")
    except ZeroDivisionError:
        print("  [通过] 频率为零时正确抛出异常")

    try:
        convert_period_to_frequency(0, 's')
        print("  [失败] 应该抛出 ZeroDivisionError")
    except ZeroDivisionError:
        print("  [通过] 周期为零时正确抛出异常")

    # 测试无效单位
    try:
        convert_frequency_to_period(100, 'XYZ')
        print("  [失败] 应该抛出 ValueError")
    except ValueError:
        print("  [通过] 无效单位时正确抛出异常")

    print("\n" + "=" * 60)
    print("测试完成！")
    print("=" * 60 + "\n")


# ==================== 程序入口 ====================

if __name__ == "__main__":
    # 检查是否运行测试
    if len(sys.argv) > 1 and sys.argv[1] == '--test':
        run_tests()
    else:
        main()
