# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 07
# @Author   : Ranshi
# @File     : 322. 凑零钱问题.py
from typing import List


class Solution:
    def coinChange(coins: List[int], amount: int):
        def dp(n):
            if n == 0:
                return 0
            if n < 0:
                return -1
            res = float("INF")
            for coin in coins:
                subproblem = dp(n - coin)
                if subproblem == -1:
                    continue
                res = min(res, 1 + dp(n - coin))
            return res

        return dp(amount)


if __name__ == "__main__":
    s = Solution()
    print(s.coinChange({1, 2, 5}, 11))
