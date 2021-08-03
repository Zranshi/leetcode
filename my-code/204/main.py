# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 02
# @Author   : Ranshi
# @File     : 204. 计数质数.py
class Solution:
    def countPrimes(self, n: int) -> int:
        primes = [True] * (n + 1)
        p = 2
        while p * p <= n:
            if primes[p]:
                for i in range(p * 2, n + 1, p):
                    primes[i] = False
            p += 1
        return primes[2:-1].count(True)


if __name__ == "__main__":
    s = Solution()
    for i in range(100):
        print(i, ":", s.countPrimes(i))
