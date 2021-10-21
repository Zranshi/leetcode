#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/10/20 23:08
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 剑指 Offer 57 - II. 和为s的连续正数序列
from typing import List


class Solution:
    def findContinuousSequence(self, target: int):
        i, j, res = 1, 2, []
        while i < j:
            j = (-1 + (1 + 4 * (2 * target + i ** 2 - i)) ** 0.5) / 2
            if i < j and j == int(j):
                res.append(list(range(i, int(j) + 1)))
            i += 1
        return res


if __name__ == "__main__":
    print(Solution().findContinuousSequence(target=9))
