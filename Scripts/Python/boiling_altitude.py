"""
从水的沸点计算海拔高度(大致估算)
========================================
基于克劳修斯-克拉佩龙方程 + 标准大气压高公式
"""

import math


def boiling_point_to_pressure(t_C: float) -> float:
    """
    根据水的沸点（摄氏度）计算当地大气压（kPa）。
    
    参数:
        t_C : 实测沸点，单位 °C
        
    返回:
        当地大气压，单位 kPa
    
    原理：克劳修斯-克拉佩龙方程的简化形式
          ln(P/P0) = ΔH_vap/R * (1/T0 - 1/T)
    """
    T0 = 373.15          # 标准沸点，K
    P0 = 101.325         # 标准大气压，kPa
    delta_H_over_R = 4888.0  # ΔH_vap / R ≈ 40656 / 8.31446

    T = t_C + 273.15      # 转换为开尔文
    if T <= 0:
        raise ValueError("沸点必须大于绝对零度")

    ln_ratio = delta_H_over_R * (1.0 / T0 - 1.0 / T)
    pressure = P0 * math.exp(ln_ratio)
    return pressure


def pressure_to_altitude(p_kPa: float, t_surface_C: float = 15.0) -> float:
    """
    根据当地大气压（kPa）和地表气温（°C）计算海拔高度（米）。
    
    参数:
        p_kPa       : 当地大气压，单位 kPa
        t_surface_C : 地表气温，单位 °C，默认为标准大气 15°C
        
    返回:
        海拔高度，单位 米
        
    原理：标准大气压高公式（对流层，0~11 km）
          P = P0 * (1 - L*h/T0)^(gM/RL)
    """
    P0 = 101.325          # 海平面标准大气压，kPa
    T0 = 288.15           # 海平面标准温度，K（= 15°C）
    L = 0.0065            # 温度递减率，K/m
    exponent = 5.25588    # gM/(RL)

    # 如果提供了实际地表气温，则修正 T0
    T0_actual = t_surface_C + 273.15

    ratio = p_kPa / P0
    if ratio <= 0 or ratio > 1:
        raise ValueError("气压比应在 (0, 1] 范围内")

    # 逆推高度
    altitude = (T0_actual / L) * (1 - ratio ** (1.0 / exponent))
    return altitude


def boiling_point_to_altitude(t_C: float, t_surface_C: float = 15.0) -> float:
    """
    一步计算：从沸点（°C）直接得到海拔高度（米）。
    
    参数:
        t_C         : 实测沸点，°C
        t_surface_C : 地表气温，°C（用于修正，默认 15°C）
        
    返回:
        海拔高度，米
    """
    p = boiling_point_to_pressure(t_C)
    h = pressure_to_altitude(p, t_surface_C)
    return h


# ===================== 示例用法 =====================
if __name__ == "__main__":
    print("=" * 50)
    print("水的沸点 → 海拔高度计算器")
    print("=" * 50)

    while True:
        try:
            inp = input("\n请输入沸点温度 (°C，输入 q 退出): ").strip()
            if inp.lower() in ('q', 'quit', 'exit'):
                break
            t_boil = float(inp)
            if t_boil <= 0 or t_boil > 110:
                print("沸点通常应在 0~110°C 之间，请重新输入")
                continue

            # 可选：输入地表气温
            inp_temp = input("请输入当前地表气温 (°C，直接回车则使用默认 15°C): ").strip()
            t_surf = float(inp_temp) if inp_temp else 15.0

            alt = boiling_point_to_altitude(t_boil, t_surf)
            press = boiling_point_to_pressure(t_boil)

            print(f"\n▶ 计算结果:")
            print(f"  当地大气压: {press:.2f} kPa")
            print(f"  估算海拔  : {alt:.0f} 米 ({alt/1000:.2f} 公里)")

        except ValueError as e:
            print(f"输入错误: {e}")
        except Exception as e:
            print(f"计算异常: {e}")

    print("\n再见！")