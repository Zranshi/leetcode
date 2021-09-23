# -*- coding:utf-8 -*-
# @Time     : 2021/7/20 09: 21
# @Author   : Ranshi
# @File     : main.py
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        length = len(nums)
        for idx_num in range(0, 1 << length):
            idx = []
            for i in range(length):
                if (idx_num >> i) % 2 == 1:
                    idx.append(nums[i])
            res.append(idx)
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.subsets(nums=[1, 2, 3]))
