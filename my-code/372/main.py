#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/12/05 08:54
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 372. 超级次方
# 你的任务是计算 a^b 对 1337 取模，a 是一个正整数，b 是一个非常大的正整数且会以数组形式给出。
class Solution:
    def superPow(self, a: int, b: list[int]) -> int:
        return pow(a, int("".join(map(str, b))), 1337)


if __name__ == "__main__":
    print(Solution().superPow(a=2147483647, b=[2, 0, 0]))
