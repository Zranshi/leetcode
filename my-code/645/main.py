# -*- coding:utf-8 -*-
# @Time     : 2021/7/4 12: 31
# @Author   : Ranshi
# @File     : 123.py
from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        length, repeat = len(nums), 0
        nums.sort()
        for i in range(length - 1):
            if nums[i] == nums[i + 1]:
                repeat = nums[i]
        _sum = (1 + length) * length // 2
        lost = repeat + _sum - sum(nums)
        return [repeat, lost]


if __name__ == "__main__":
    s = Solution()
    print(s.findErrorNums([1, 5, 3, 2, 2, 7, 6, 4, 8, 9]))
