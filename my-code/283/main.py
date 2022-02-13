# -*- coding:utf-8 -*-
# @Time     : 2021/07/27 19:28
# @Author   : Ranshi
# @File     : 123.py

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero_num = 0
        for idx in range(len(nums)):
            if nums[idx] == 0:
                zero_num += 1
            else:
                nums[idx - zero_num] = nums[idx]
        for idx in range(-1, -zero_num - 1, -1):
            nums[idx] = 0


if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    Solution().moveZeroes(nums)
    print(nums)
