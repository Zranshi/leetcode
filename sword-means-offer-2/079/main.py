# -*- coding: UTF-8 -*-
# @Time     : 2023/01/31 19:50
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 剑指 Offer II 079. 所有子集
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        total = 2 ** len(nums)
        return [
            [v for j, v in enumerate(nums) if i & (1 << j)]
            for i in range(total)
        ]


if __name__ == "__main__":
    print(Solution().subsets(nums=[1, 2, 3]))
