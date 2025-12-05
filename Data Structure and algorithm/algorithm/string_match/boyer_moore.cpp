/**
 * 字符串匹配算法-Boyer Moore算法
 * 参考：https://oi-wiki.org/string/bm/
 */
#include <string>
#include <iostream>
using namespace std;

#define ASIZE 256 // ASCII字母的种类

// 1.坏后缀数组建立，类似于字典（map），用于判断坏字符在pattern中的位置
void generateBC(string str, int bc[])
{
    for (int i = 0; i < ASIZE; i++)
        bc[i] = -1;

    for (int i = 0; i < str.size(); i++)
        bc[str[i]] = i;
}

// 2.好后缀数组的建立,suffix为后缀字符对应前面的位置，prefix存储：是否存在匹配的前缀字串
void generateGS(string str, int suffix[], bool prefix[])
{
    int n = str.size();
    for (int i = 0; i < n - 1; i++)
    {
        suffix[i] = -1;
        prefix[i] = false;
    }

    for (int i = 0; i < n - 1; i++)
    {
        int j = i;                                 // 从第一个字符开始遍历，str[j]
        int k = 0;                                 // 最后一个字符的变化，对应下面的str[n - 1 - k]
        while (j >= 0 && str[j] == str[n - 1 - k]) // 和最后一个字符对比，相等则倒数第二个
        {
            j--;
            k++;
            suffix[k] = j + 1; // 如果k=1，则是一个字符长度的后缀对应匹配位置的值
        }
        if (j == -1) // 说明有前缀字符对应
            prefix[k] = true;
    }
}

// 3.返回好后缀移动的次数,index为坏字符位置-其后面就是好后缀，size为str大小
int getGsMove(int suffix[], bool prefix[], int index, int size)
{
    int len = size - index - 1;         // 好字符的长度，因为index为坏字符位置，所以要多减1
    if (suffix[len] != -1)              // 当前len长度的后缀坏字符串前边有匹配的字符
        return index + 1 - suffix[len]; // 后移位数 = 好后缀的位置(index + 1) - 搜索词中的上一次出现位置

    // index为坏字符，index+1为好后缀，index+2为子好后缀
    for (int i = index + 2; i < size; i++)
    {
        if (prefix[size - i]) // 因为prefix从1开始
            return i;         // 移动当前位置离前缀位置，acba-对应a移动3
    }

    return 0;
}

// 4.返回找到匹配字符串的头(从0开始索引,匹配到第一个字符串就停止)，否则返回-1
int BM(string str, string pattern)
{
    int n = str.size();
    int m = pattern.size();
    int bc[ASIZE]; // 坏字符数组
    int *suffix = (int *)malloc(sizeof(int) * m);
    bool *prefix = (bool *)malloc(sizeof(bool) * m);

    generateBC(pattern, bc);
    generateGS(pattern, suffix, prefix);

    int i = 0;
    while (i <= n - m)
    {
        int j = 0;
        for (j = m - 1; j >= 0; j--)
        {
            if (pattern[j] != str[i + j]) // 从后往前匹配str和pattern
                break;
        }
        if (j < 0) // 匹配结束
            return i;
        else
        {
            int numBc = j - bc[str[i + j]]; // bc移动的位数
            int numGs = 0;
            if (j < m - 1) // 最后一个字符就是坏字符，无需判断好字符
            {
                numGs = getGsMove(suffix, prefix, j, m); // Gs移动的位数
            }
            i += numBc > numGs ? numBc : numGs;
        }
    }

    return -1;
}

int main()
{
    cout << BM("HERE IS A SIMPLE EXAMPLE", "EXAMPLE") << endl;
}
