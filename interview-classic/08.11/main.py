# -*- coding:utf-8 -*-
# @Time     : 2021/7/21 19: 24
# @Author   : Ranshi
# @File     : main.py
class Solution:
    def waysToChange(self, n: int) -> int:
        mod = 10 ** 9 + 7
        coins = [25, 10, 5, 1]

        f = [1] + [0] * n
        for coin in coins:
            for i in range(coin, n + 1):
                f[i] += f[i - coin]
        return f[n] % mod


if __name__ == '__main__':
    print(Solution().waysToChange(10))
