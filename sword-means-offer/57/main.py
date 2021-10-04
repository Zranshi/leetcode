# -*- coding: UTF-8 -*-
# @Time     : 2021/10/04 12:56
# @Author   : Ranshi
# @File     : main.py
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        while left < right:
            idx = nums[left] + nums[right]
            if idx == target:
                return [nums[left], nums[right]]
            elif idx < target:
                left += 1
            else:
                right -= 1
        return []


if __name__ == "__main__":
    print(Solution().twoSum(nums=[2, 7, 11, 15], target=9))
