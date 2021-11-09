#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/11/01 08:00
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 575. 分糖果
class Solution:
    def distributeCandies(self, candies: list[int]) -> int:
        kind = len(set(candies))
        return min(kind, len(candies) // 2)


if __name__ == "__main__":
    print(Solution().distributeCandies(candies=[1, 1, 2, 2, 3, 3]))
