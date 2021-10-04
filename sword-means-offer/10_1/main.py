# -*- coding: UTF-8 -*-
# @Time     : 2021/09/04 09:06
# @Author   : Ranshi
# @File     : main.py
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        MOD = 10 ** 9 + 7
        a, b = 1, 0
        for _ in range(1, n):
            a, b = a + b, a
        return a % MOD


if __name__ == "__main__":
    print(Solution().fib(n=5))
