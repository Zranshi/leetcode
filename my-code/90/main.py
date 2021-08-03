# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 17: 58
# @Author   : Ranshi
# @File     : 90. 子集 II.py
from itertools import combinations
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        nums.sort()
        for i in range(1, len(nums) + 1):
            iter1 = list(set(combinations(nums, i)))
            res = res + list(iter1)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.subsetsWithDup(nums=[1, 2, 2]))
