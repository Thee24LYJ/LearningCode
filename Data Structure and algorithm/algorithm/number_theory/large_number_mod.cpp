/**
 * 大数求余算法，用于计算一个非常大的数(超过long long型数字)对另一个数取模的结果
 * 参考：https://www.geeksforgeeks.org/modulus-large-number/
 */

#include <iostream>
#include <string>
#include <cmath>
#include "../../../Execution time calculation/HighPrecisionTimer.cpp"
using namespace std;

/**
 * @brief 计算大数对模数的余数(模拟手算过程)
 *
 * @param large_num 字符串形式表示的大数
 * @param mod 模数
 * @return long long 大数对模数的余数
 */
long long large_number_mod(const string &large_num, int mod)
{
    long long result = 0;
    for (int i = 0; i < large_num.size(); i++)
    {
        result = (result * 10 + large_num[i] - '0') % mod;
    }
    return result;
}

/**
 * @brief 优化版本：每次处理k位数字，减少循环次数
 *
 * @param large_num 字符串形式表示的大数
 * @param mod 模数
 * @param k_size 每次处理的数字位数
 * @return long long 大数对模数的余数
 */
long long large_number_mod_optimized(const string &large_num, int mod, int k_size)
{
    long long result = 0;
    string segment;
    for (size_t i = 0; i < large_num.size(); i += k_size)
    {
        int offset = min(k_size, static_cast<int>(large_num.size() - i));
        segment = large_num.substr(i, offset);
        result = (result * static_cast<long long>(pow(10, segment.size())) + stoi(segment)) % mod;
    }
    return result;
}

// 执行时间计算
#include <chrono>

int main()
{
    HighPrecisionTimer timer("Large Number Modulus Calculation");
    string large_num;
    int mod = 998244353; // 示例模数
    cout << "Enter a large number: ";
    cin >> large_num;
    timer.start();
    long long result = large_number_mod(large_num, mod);
    timer.stop();
    timer.print("ns");
    cout << "Result of large number mod " << mod << " is: " << result << endl;
    // 优化版本测试
    int k_size = 9; // 每次处理9位数字
    timer.start();
    long long optimized_result = large_number_mod_optimized(large_num, mod, k_size);
    timer.stop();
    timer.print("ns");
    cout << "Optimized result of large number mod " << mod << " is: " << optimized_result << endl;

    return 0;
}
