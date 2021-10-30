# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 18
# @Author   : Ranshi
# @File     : 1052. 爱生气的书店老板.py
from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        diffC = [x * item for x, item in zip(customers, grumpy)]
        maxC = [sum(diffC[0:X]), 0]
        idx_sum = sum(diffC[0:X])
        # print(diffC, maxC)
        for idx in range(1, len(diffC) - X + 1):
            idx_sum = idx_sum + diffC[idx + X - 1] - diffC[idx - 1]
            if maxC[0] < idx_sum:
                maxC[0] = idx_sum
                maxC[1] = idx
        # print(maxC)
        for i in range(maxC[1], maxC[1] + X):
            grumpy[i] = 0
        # print(grumpy)
        return sum([x * (1 - item) for x, item in zip(customers, grumpy)])


if __name__ == "__main__":
    s = Solution()
    print(
        s.maxSatisfied(
            customers=[1, 0, 1, 2, 1, 1, 7, 5],
            grumpy=[0, 1, 0, 1, 0, 1, 0, 1],
            X=3,
        )
    )
