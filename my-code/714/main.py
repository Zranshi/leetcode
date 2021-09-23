# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 12
# @Author   : Ranshi
# @File     : 714. 买卖股票的最佳时机含手续费.py
from typing import List


class Solution:
    def maxProfit1(self, prices: List[int], fee: int) -> int:
        """
        动态规划
        """
        n = len(prices)
        dp = [[0, -prices[0]]] + [[0, 0] for _ in range(n - 1)]
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i] - fee)
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        return dp[n - 1][0]

    def maxProfit2(self, prices: List[int], fee: int) -> int:
        """
        dp简化版本
        """
        n = len(prices)
        sell, buy = 0, -prices[0]
        for i in range(1, n):
            sell, buy = max(sell, buy + prices[i] - fee), max(
                buy, sell - prices[i]
            )
        return 0

    def maxProfit(self, prices: List[int], fee: int) -> int:
        """
        贪心
        """
        n = len(prices)
        buy = prices[0] + fee
        profit = 0
        for i in range(1, n):
            if prices[i] + fee < buy:
                buy = prices[i] + fee
            elif prices[i] > buy:
                profit += prices[i] - buy
                buy = prices[i]
        return profit


if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit(prices=[1, 3, 2, 8, 4, 9], fee=2))
