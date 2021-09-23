# -*- coding:utf-8 -*-
# @Time     : 2021/7/17 10: 22
# @Author   : Ranshi
# @File     : main.py
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ant, res = 0, nums[0]
        for x in nums:
            ant = max(ant + x, x)
            res = max(res, ant)
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))
