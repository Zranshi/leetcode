# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 09
# @Author   : Ranshi
# @File     : 454. 四数相加 II.py
from itertools import product
from typing import List


class Solution:
    def fourSumCount(
        self, A: List[int], B: List[int], C: List[int], D: List[int]
    ) -> int:
        res = 0
        ab_map = dict()
        for a, b in product(A, B):
            ab_map[a + b] = ab_map.get(a + b, 0) + 1
        for c, d in product(C, D):
            s = -(c + d)
            if s in ab_map:
                res += ab_map[s]
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.fourSumCount(A=[1, 2], B=[-2, -1], C=[-1, 2], D=[0, 2]))
