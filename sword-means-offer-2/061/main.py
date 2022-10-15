# -*- coding: UTF-8 -*-
# @Time     : 2022/10/15 17:24
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 剑指 Offer II 061. 和最小的 k 个数对
import heapq


class Pair:
    def __init__(self, a: int, b: int) -> None:
        self.a = a
        self.b = b
        self.sum = -a - b

    def __lt__(self, other: "Pair"):
        return self.sum < other.sum

    def export(self):
        return [self.a, self.b]


class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        lst: list[Pair] = []
        for a in nums1:
            for b in nums2:
                heapq.heappush(lst, Pair(a, b))
                while len(lst) > k:
                    heapq.heappop(lst)
        return [item.export() for item in lst]


print(Solution().kSmallestPairs(nums1=[1, 7, 11], nums2=[2, 4, 6], k=3))
