#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/11/12 07:37
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 375. 猜数字大小 II
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        f = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n - 1, 0, -1):
            for j in range(i + 1, n + 1):
                f[i][j] = min(k + max(f[i][k - 1], f[k + 1][j]) for k in range(i, j))
        return f[1][n]


if __name__ == "__main__":
    print(Solution().getMoneyAmount(n=10))
