# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 20
# @Author   : Ranshi
# @File     : 1438. 绝对差不超过限制的最长连续子数组.py
from typing import List

from sortedcontainers import SortedList


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        s = SortedList()
        left = ret = 0

        for right in range(len(nums)):
            s.add(nums[right])
            while s[-1] - s[0] > limit:
                s.remove(nums[left])
                left += 1
            ret = max(ret, right - left + 1)

        return ret


if __name__ == "__main__":
    s = Solution()
    print(s.longestSubarray(nums=[10, 1, 2, 4, 7, 2], limit=5))
