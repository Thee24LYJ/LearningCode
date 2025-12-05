/**
 * 大数求余算法，用于计算一个非常大的数(超过long long型数字)对另一个数取模的结果
 * 参考：https://www.geeksforgeeks.org/modulus-large-number/
 */

#include <iostream>
#include <string>
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

int main()
{
    string large_num;
    int mod = 998244353; // 示例模数
    cout << "Enter a large number: ";
    cin >> large_num;
    long long result = large_number_mod(large_num, mod);
    cout << "Result of large number mod " << mod << " is: " << result << endl;

    return 0;
}
