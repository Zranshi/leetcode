#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/12/12 19:55
# @Author   : Ranshi
# @File     : 123.py
# @Doc      : 剑指 Offer II 003. 前 n 个数字二进制中 1 的个数
class Solution:
    def countBits(self, n: int) -> list[int]:
        bits: list[int] = [0] * (n + 1)
        for i in range(1, n + 1):
            bits[i] = bits[i & (i - 1)] + 1
        return bits


if __name__ == "__main__":
    print(Solution().countBits(n=2))
