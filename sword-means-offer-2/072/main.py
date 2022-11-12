# -*- coding: UTF-8 -*-
# @Time     : 2022/11/12 22:10
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 剑指 Offer II 072. 求平方根
class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left <= right:
            mid = (left + right) // 2
            if mid**2 > x:
                right = mid - 1
            else:
                left = mid + 1
        return right


print(Solution().mySqrt(9))
