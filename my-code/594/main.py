#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/11/20 08:25
# @Author   : Ranshi
# @File     : 123.py
# @Doc      : 594. 最长和谐子序列
class Solution:
    def findLHS(self, nums: list[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        left, res = 0, 0
        for right in range(len(nums)):
            while nums[right] - nums[left] > 1:
                left += 1
            if nums[right] - nums[left] == 1:
                res = max(res, right - left + 1)
        return res


if __name__ == "__main__":
    print(Solution().findLHS(nums=[1, 1, 1, 1]))
