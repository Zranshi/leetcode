# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 17: 53
# @Author   : Ranshi
# @File     : 75. 颜色分类.py
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums[:] = nums.count(0) * [0] + nums.count(1) * [1] + nums.count(2) * [2]


if __name__ == "__main__":
    s = Solution()
    s.sortColors(nums=[2, 0, 2, 1, 1, 0])
