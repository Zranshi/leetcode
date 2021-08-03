# -*- coding:utf-8 -*-
# @Time     : 2021/6/10 13:46
# @Author   : Ranshi
# @File     : 518. 零钱兑换 II.py
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0 for _ in range(amount + 1)]
        dp[0] = 1
        for coin in coins:
            for i in range(amount + 1):
                if i + coin <= amount:
                    dp[i + coin] += dp[i]
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.change(amount=10, coins=[10]))
