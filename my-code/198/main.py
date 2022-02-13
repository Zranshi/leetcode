# -*- coding:utf-8 -*-
# @Time     : 2021/07/27 20:24
# @Author   : Ranshi
# @File     : 123.py
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        dp: List[int] = [0] * len(nums)
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        return dp[-1]


if __name__ == "__main__":
    print(Solution().rob([1, 2, 3, 1]))
