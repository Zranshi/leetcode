#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/10/30 07:04
# @Author   : Ranshi
# @File     : 123.py
# @Doc      : 260. 只出现一次的数字 III
class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        xorsum = 0
        for num in nums:
            xorsum ^= num

        lsb = xorsum & (-xorsum)
        type1 = type2 = 0
        for num in nums:
            if num & lsb:
                type1 ^= num
            else:
                type2 ^= num

        return [type1, type2]


if __name__ == "__main__":
    print(Solution().singleNumber(nums=[1, 2, 1, 3, 2, 5]))
