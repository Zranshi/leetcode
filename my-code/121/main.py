# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 01
# @Author   : Ranshi
# @File     : 121. 买卖股票的最佳时机.py
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        _max = 0
        _min = float('inf')
        for price in prices:
            _max = max(price - _min, _max)
            _min = min(price, _min)
        return int(_max)


if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([7, 1, 5, 3, 6, 4]))
