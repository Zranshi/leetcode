# -*- coding:utf-8 -*-
# @Time     : 2021/7/20 09: 08
# @Author   : Ranshi
# @File     : main.py
from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for i in range(0, len(nums) // 2):
            res = max(res, nums[i] + nums[-(i + 1)])
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.minPairSum(nums=[3, 5, 2, 3]))
