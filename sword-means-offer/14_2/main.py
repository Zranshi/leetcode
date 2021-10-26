#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/10/23 08:23
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 剑指 Offer 14- II. 剪绳子 II
class Solution:
    def cuttingRope(self, n: int) -> int:
        if n <= 3:
            return n - 1
        a, b, p, x, rem = n // 3 - 1, n % 3, 1000000007, 3, 1
        while a > 0:
            if a % 2:
                rem = (rem * x) % p
            x = x ** 2 % p
            a //= 2
        if b == 0:
            return (rem * 3) % p  # = 3^(a+1) % p
        if b == 1:
            return (rem * 4) % p  # = 3^a * 4 % p
        return (rem * 6) % p  # = 3^(a+1) * 2  % p
