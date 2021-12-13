#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/12/12 21:06
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 1920. 基于排列构建数组
class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        res: list[int] = [0] * len(nums)
        for i, v in enumerate(nums):
            res[i] = nums[v]
        return res


if __name__ == "__main__":
    print(Solution().buildArray(nums=[0, 2, 1, 5, 3, 4]))
