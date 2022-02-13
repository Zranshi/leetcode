#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/11/30 08:10
# @Author   : Ranshi
# @File     : 123.py
# @Doc      : 400. 第 N 位数字
class Solution:
    def totalDigits(self, length: int) -> int:
        digits = 0
        curCount = 9
        for curLength in range(1, length + 1):
            digits += curLength * curCount
            curCount *= 10
        return digits

    def findNthDigit(self, n: int) -> int:
        low, high = 1, 9
        while low < high:
            mid = (low + high) // 2
            if self.totalDigits(mid) < n:
                low = mid + 1
            else:
                high = mid
        d = low
        prevDigits = self.totalDigits(d - 1)
        index = n - prevDigits - 1
        start = 10 ** (d - 1)
        num = start + index // d
        digitIndex = index % d
        return num // 10 ** (d - digitIndex - 1) % 10


if __name__ == "__main__":
    print(Solution().findNthDigit(n=3))
