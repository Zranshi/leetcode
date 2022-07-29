# -*- coding: UTF-8 -*-
# @Time     : 2021/08/28 08:58
# @Author   : Ranshi
# @File     : 123.py


class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums


if __name__ == "__main__":
    print(Solution().runningSum(nums=[1]))
