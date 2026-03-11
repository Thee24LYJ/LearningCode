/**
 * @file convex_hull.cpp
 * @author thee (1579290423@qq.com)
 * @brief
 * @version 0.1
 * @date 2026-01-03
 *
 * @copyright Copyright (c) 2026
 *
 */

#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <Eigen/Dense>

// update later
using namespace std;

using Eigen::Vector2d;

// 2D cross product (z-component only)
inline double cross(const Vector2d &a, const Vector2d &b)
{
    return a.x() * b.y() - a.y() * b.x();
}

vector<int> andrew(vector<Vector2d> &points)
{
    int tp = 0; // 初始化栈
    vector<int> stk(points.size());
    sort(points.begin(), points.end(), [](const Vector2d &a, const Vector2d &b)
         {
        if (a.x() != b.x()) return a.x() < b.x();
        return a.y() < b.y(); }); // 按照 x 坐标排序
    stk[++tp] = 1;
    // 栈内添加第一个元素，且不更新used， 使得1在最后封闭凸包时也对单调栈更新
    for (int i = 2; i < static_cast<int>(points.size()); i++)
    {
        while (tp >= 2 && cross(points[stk[tp]] - points[stk[tp - 1]], points[i] - points[stk[tp]]) <= 0)
        {
            tp--;
            stk.pop_back();
        }
        stk.push_back(i);
        tp++;
    }
}



int main()
{
    int tp = 0; // 初始化栈
    vector<int> stk;
    return 0;
}
