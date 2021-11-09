# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 10
# @Author   : Ranshi
# @File     : 509. 斐波那契数列.py
import math


class Solution:
    def fib(self, N: int) -> int:
        return round(pow((1 + math.sqrt(5)) / 2, N) / math.sqrt(5))


if __name__ == "__main__":
    s = Solution()
    n = input()
    print(s.fib(int(n)))
