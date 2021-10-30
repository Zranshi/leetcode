#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/10/21 09:40
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 剑指 Offer 59 - I. 滑动窗口的最大值
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        n = len(nums)
        prefixMax, suffixMax = [0] * n, [0] * n
        for i in range(n):
            prefixMax[i] = nums[i] if i % k == 0 else max(prefixMax[i - 1], nums[i])
        for i in range(n - 1, -1, -1):
            if i == n - 1 or (i + 1) % k == 0:
                suffixMax[i] = nums[i]
            else:
                suffixMax[i] = max(suffixMax[i + 1], nums[i])

        return [max(suffixMax[i], prefixMax[i + k - 1]) for i in range(n - k + 1)]


if __name__ == "__main__":
    print(Solution().maxSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))
