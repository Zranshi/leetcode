#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/10/14 07:29
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 剑指 Offer 56 - I. 数组中数字出现的次数
import functools
from typing import List


class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        ret = functools.reduce(lambda x, y: x ^ y, nums)
        h = 1
        while h & ret == 0:
            h <<= 1
        a, b = 0, 0
        for x in nums:
            if x & h:
                a ^= x
            else:
                b ^= x
        return [a, b]


if __name__ == "__main__":
    print(Solution().singleNumbers(nums=[4, 1, 4, 6]))
