/**
 * @file HighPrecisionTimer.cpp
 * @author thee (1579290423@qq.com)
 * @brief 高精度计时器类，基于C++11的chrono库实现
 * @version 0.1
 * @date 2025-12-09
 *
 * @copyright Copyright (c) 2025
 *
 */
#include <iostream>
#include <chrono>
#include <string>

class HighPrecisionTimer
{
private:
    std::chrono::high_resolution_clock::time_point start_time;
    std::chrono::high_resolution_clock::time_point end_time;
    std::string timer_name;

public:
    // 构造函数
    explicit HighPrecisionTimer(const std::string &name = "") : timer_name(name)
    {
        start();
    }

    // 开始计时
    void start()
    {
        start_time = std::chrono::high_resolution_clock::now();
    }

    // 停止计时
    void stop()
    {
        end_time = std::chrono::high_resolution_clock::now();
    }

    // 获取纳秒
    long long get_nanoseconds() const
    {
        return std::chrono::duration_cast<std::chrono::nanoseconds>(end_time - start_time).count();
    }

    // 获取微秒
    long long get_microseconds() const
    {
        return std::chrono::duration_cast<std::chrono::microseconds>(end_time - start_time).count();
    }

    // 获取毫秒
    long long get_milliseconds() const
    {
        return std::chrono::duration_cast<std::chrono::milliseconds>(end_time - start_time).count();
    }

    // 获取秒（double类型，更高精度）
    double get_seconds() const
    {
        return std::chrono::duration<double>(end_time - start_time).count();
    }

    // 打印结果
    void print(const std::string &unit = "auto") const
    {
        auto ns = get_nanoseconds();

        if (unit == "ns" || (unit == "auto" && ns < 1000))
        {
            std::cout << timer_name << "耗时: " << ns << " ns" << std::endl;
        }
        else if (unit == "us" || (unit == "auto" && ns < 1000000))
        {
            std::cout << timer_name << "耗时: " << get_microseconds() << " us" << std::endl;
        }
        else if (unit == "ms" || (unit == "auto" && ns < 1000000000))
        {
            std::cout << timer_name << "耗时: " << get_milliseconds() << " ms" << std::endl;
        }
        else
        {
            std::cout << timer_name << "耗时: " << get_seconds() << " s" << std::endl;
        }
    }

    // 析构函数自动打印
    ~HighPrecisionTimer()
    {
        if (!timer_name.empty())
        {
            print();
        }
    }
};