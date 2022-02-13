#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/10/13 09:15
# @Author   : Ranshi
# @File     : 123.py
# @Doc      : 剑指 Offer 65. 不用加减乘除做加法
class Solution:
    def add(self, a: int, b: int) -> int:
        x = 0xFFFFFFFF
        a, b = a & x, b & x
        while b != 0:
            a, b = (a ^ b), (a & b) << 1 & x
        return a if a <= 0x7FFFFFFF else ~(a ^ x)


if __name__ == "__main__":
    print(Solution().add(a=1, b=1))
