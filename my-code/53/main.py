# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 17: 52
# @Author   : Ranshi
# @File     : 53. 最大子序和.py
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res, ans = -float("inf"), 0
        for x in nums:
            ans += x
            res = max(ans, res)
            ans = max(ans, 0)
        return int(res)


if __name__ == "__main__":
    s = Solution()
    print(s.maxSubArray(nums=[-2]))
