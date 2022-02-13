# -*- coding: UTF-8 -*-
# @Time     : 2021/10/04 12:41
# @Author   : Ranshi
# @File     : 123.py
from typing import List


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        while left < right:
            while left < right and nums[left] & 1 == 1:
                left += 1
            while left < right and nums[right] & 1 == 0:
                right -= 1
            nums[left], nums[right] = nums[right], nums[left]
        return nums


if __name__ == "__main__":
    print(Solution().exchange(nums=[1, 2, 3, 4]))
