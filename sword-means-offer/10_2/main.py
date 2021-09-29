# -*- coding: UTF-8 -*-
# @Time     : 2021/09/29 19:01
# @Author   : Ranshi
# @File     : main.py
class Solution:
    def numWays(self, n: int) -> int:
        if n in {0, 1}:
            return 1
        MOD = 10 ** 9 + 7
        a, b = 1, 1
        for _ in range(1, n):
            a, b = a + b, a
        return a % MOD


if __name__ == "__main__":
    print(Solution().numWays(44))
