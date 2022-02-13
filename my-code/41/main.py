# -*- coding: UTF-8 -*-
# @Time     : 2021/09/04 12:28
# @Author   : Ranshi
# @File     : 123.py


from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1


if __name__ == "__main__":
    print(Solution().firstMissingPositive(nums=[7, 8, 9, 11, 12]))
