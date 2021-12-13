#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 24
# @Author   : Ranshi
# @File     : 1835. 所有数对按位与结果的异或和.py
from typing import List


class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        ans = 0

        for k in range(30, -1, -1):
            cnt1 = sum(1 for num in arr1 if num & (1 << k))
            cnt2 = sum(1 for num in arr2 if num & (1 << k))
            if cnt1 % 2 == 1 and cnt2 % 2 == 1:
                ans |= 1 << k

        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.getXORSum(arr1=[1, 2, 3], arr2=[6, 5]))
