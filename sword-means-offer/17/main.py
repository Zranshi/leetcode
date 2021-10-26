#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/10/22 08:12
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 剑指 Offer 17. 打印从1到最大的n位数
class Solution:
    def printNumbers(self, n: int) -> list[int]:
        return list(range(1, 10 ** n))


if __name__ == "__main__":
    print(Solution().printNumbers(n=5))
