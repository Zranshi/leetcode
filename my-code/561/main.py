# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 11
# @Author   : Ranshi
# @File     : 561. 数组拆分 I.py
from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[::2])


if __name__ == '__main__':
    s = Solution()
    print(s.arrayPairSum(nums=[6, 2, 6, 5, 1, 2]))
