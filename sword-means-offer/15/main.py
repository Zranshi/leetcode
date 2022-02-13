#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/10/13 09:13
# @Author   : Ranshi
# @File     : 123.py
# @Doc      : 剑指 Offer 15. 二进制中1的个数
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            if n & 1:
                res += 1
            n >>= 1
        return res


if __name__ == "__main__":
    print(Solution().hammingWeight(11))
