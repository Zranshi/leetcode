# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 12
# @Author   : Ranshi
# @File     : 703. 数据流中的第 K 大元素.py
import heapq
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)
        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val)
        elif self.nums[0] < val:
            heapq.heapreplace(self.nums, val)
        return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


if __name__ == '__main__':
    s = KthLargest(3, [4, 5, 8, 2])
    print(s.add(3))
    print(s.add(5))
    print(s.add(10))
    print(s.add(9))
    print(s.add(4))
