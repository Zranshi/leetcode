# -*- coding:utf-8 -*-
# @Time     : 2021/7/23 12: 57
# @Author   : Ranshi
# @File     : 123.py
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        from bisect import bisect_left

        res = []
        ri = bisect_left(nums, 0)
        le = ri - 1
        while le >= 0 and ri < len(nums):
            if abs(nums[le]) < nums[ri]:
                res.append(nums[le] ** 2)
                le -= 1
            else:
                res.append(nums[ri] ** 2)
                ri += 1
        while le >= 0:
            res.append(nums[le] ** 2)
            le -= 1
        while ri < len(nums):
            res.append(nums[ri] ** 2)
            ri += 1
        return res


if __name__ == "__main__":
    print(Solution().sortedSquares(nums=[-1]))
