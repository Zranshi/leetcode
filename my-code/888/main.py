# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 16
# @Author   : Ranshi
# @File     : 888. 公平的糖果棒交换.py
from typing import List


class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        res = (sum(A) - sum(B)) // 2
        d = set(A)
        for x in B:
            if x + res in d:
                return [x + res, x]


if __name__ == "__main__":
    s = Solution()
    print(s.fairCandySwap(A=[1, 2], B=[2, 3]))
