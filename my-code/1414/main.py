#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/10/31 18:00
# @Author   : Ranshi
# @File     : 123.py
# @Doc      : 1414. 和为 K 的最少斐波那契数字数目
class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        a = b = 1
        fibo = [a, b]
        while a + b <= k:
            fibo.append(a + b)
            a, b = b, a + b
        ans = 0
        for num in fibo[::-1]:
            if k >= num:
                ans += 1
                k -= num
        return ans


if __name__ == "__main__":
    print(Solution().findMinFibonacciNumbers(k=7))
