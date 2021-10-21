#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/10/20 22:22
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 剑指 Offer 14- I. 剪绳子
import math


class Solution:
    def cuttingRope(self, n: int) -> int:
        if n <= 3:
            return n - 1
        a, b = n // 3, n % 3
        if b == 0:
            return int(math.pow(3, a))
        if b == 1:
            return int(math.pow(3, a - 1) * 4)
        return int(math.pow(3, a) * 2)


if __name__ == "__main__":
    print(Solution().cuttingRope(2))
