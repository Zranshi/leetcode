# -*- coding: UTF-8 -*-
# @Time     : 2022/10/15 17:18
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 剑指 Offer II 060. 出现频率最高的 k 个数字
from collections import Counter


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        c = Counter(nums)
        return sorted(c.keys(), key=lambda x: c[x], reverse=True)[:k]


print(Solution().topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2))
