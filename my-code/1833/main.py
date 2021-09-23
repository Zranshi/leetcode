# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 24
# @Author   : Ranshi
# @File     : 1833. 雪糕的最大数量.py
from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        res = 0
        for item in costs:
            if item <= coins:
                res += 1
                coins -= item
            else:
                break
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.maxIceCream(costs=[1, 3, 2, 4, 1], coins=7))
