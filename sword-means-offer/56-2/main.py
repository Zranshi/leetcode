#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/10/14 08:39
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 剑指 Offer 56 - II. 数组中数字出现的次数 II
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counts = [0] * 32
        for num in nums:
            for j in range(32):
                counts[j] += num & 1
                num >>= 1
        res, m = 0, 3
        for i in range(32):
            res <<= 1
            res |= counts[31 - i] % m
        return res if counts[31] % m == 0 else ~(res ^ 0xFFFFFFFF)


if __name__ == "__main__":
    print(Solution().singleNumber(nums=[3, 4, 3, 3]))
