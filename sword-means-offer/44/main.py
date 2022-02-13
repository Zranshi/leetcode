#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/10/23 08:25
# @Author   : Ranshi
# @File     : 123.py
# @Doc      : 剑指 Offer 44. 数字序列中某一位的数字
class Solution:
    def findNthDigit(self, n: int) -> int:
        digit, start, count = 1, 1, 9
        while n > count:  # 1.
            n -= count
            start *= 10
            digit += 1
            count = 9 * start * digit
        num = start + (n - 1) // digit  # 2.
        return int(str(num)[(n - 1) % digit])  # 3.
