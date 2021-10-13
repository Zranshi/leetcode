#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/10/13 09:02
# @Author   : Ranshi
# @File     : main.py
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        res = 1
        if n < 0:
            x, n = 1 / x, -n
        while n:
            if n & 1:
                res *= x
            x *= x
            n >>= 1
        return res


if __name__ == "__main__":
    print(Solution().myPow(x=2.00000, n=10))
