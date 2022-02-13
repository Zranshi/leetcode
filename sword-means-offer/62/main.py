#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/10/20 23:21
# @Author   : Ranshi
# @File     : 123.py
# @Doc      : 剑指 Offer 62. 圆圈中最后剩下的数字
class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        f = 0
        for i in range(2, n + 1):
            f = (m + f) % i
        return f


if __name__ == "__main__":
    print(Solution().lastRemaining(n=5, m=3))
