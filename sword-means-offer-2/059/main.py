# -*- coding: UTF-8 -*-
# @Time     : 2022/10/15 14:57
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 剑指 Offer II 059. 数据流的第 K 大数值
import heapq


class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.que = nums
        self.k = k
        heapq.heapify(self.que)

    def add(self, val: int) -> int:
        heapq.heappush(self.que, val)
        while len(self.que) > self.k:
            heapq.heappop(self.que)
        return self.que[0]


kl = KthLargest(3, [4, 5, 8, 2])
print(kl.add(3))
print(kl.add(5))
print(kl.add(10))
print(kl.add(9))
print(kl.add(4))
