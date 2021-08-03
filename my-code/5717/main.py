# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 24
# @Author   : Ranshi
# @File     : 5717. 最少操作使数组递增.py
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        length = len(nums)
        if length < 2:
            return 0
        for i in range(1, length):
            if nums[i] <= nums[i - 1]:
                res += nums[i - 1] - nums[i] + 1
                nums[i] = nums[i - 1] + 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.minOperations(nums=[1, 5, 2, 4, 1]))
