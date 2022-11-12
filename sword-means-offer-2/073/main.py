# -*- coding: UTF-8 -*-
# @Time     : 2022/11/12 22:21
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 剑指 Offer II 073. 狒狒吃香蕉
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def check(x: int) -> bool:
            day = 0
            for pile in piles:
                day += pile // x
                if pile % x != 0:
                    day += 1
            return day <= h

        left, right = 1, max(piles)
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left


print(Solution().minEatingSpeed(piles=[3, 6, 7, 11], h=8))
