# -*- coding: UTF-8 -*-
# @Time     : 2021/09/29 20:02
# @Author   : Ranshi
# @File     : 123.py
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        res = 0
        for right in range(len(prices)):
            res = max(res, prices[right] - prices[left])
            left = right if prices[right] < prices[left] else left
        return res


if __name__ == "__main__":
    print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
