#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/10/21 11:54
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 剑指 Offer 60. n个骰子的点数
class Solution:
    def dicesProbability(self, n: int) -> list[float]:
        dp = [1 / 6] * 6
        for i in range(2, n + 1):
            tmp = [0] * (5 * i + 1)
            for j in range(len(dp)):
                for k in range(6):
                    tmp[j + k] += dp[j] / 6
            dp = tmp
        return dp


if __name__ == "__main__":
    print(Solution().dicesProbability(2))
