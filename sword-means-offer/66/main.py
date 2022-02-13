#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/10/15 08:08
# @Author   : Ranshi
# @File     : 123.py
# @Doc      : 剑指 Offer 66. 构建乘积数组
from typing import List


class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        b, tmp = [1] * len(a), 1
        for i in range(1, len(a)):
            b[i] = b[i - 1] * a[i - 1]  # 下三角
        for i in range(len(a) - 2, -1, -1):
            tmp *= a[i + 1]  # 上三角
            b[i] *= tmp  # 下三角 * 上三角
        return b


if __name__ == "__main__":
    print(Solution().constructArr([1, 2, 3, 4, 5]))
