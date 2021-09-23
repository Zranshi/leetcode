# -*- coding:utf-8 -*-
# @Time     : 2021/5/29 22:39
# @Author   : Ranshi
# @File     : 5755. 数组中最大数对和的最小值.py
from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        from collections import deque

        nums.sort()
        de = deque(nums)
        _max = -float("inf")
        while de:
            x, y = de.popleft(), de.pop()
            _max = max(_max, x + y)
        return _max


if __name__ == "__main__":
    s = Solution()
    print(s.minPairSum(nums=[3, 5, 4, 2, 4, 6]))
