# -*- coding:utf-8 -*-
# @Time     : 2021/7/20 09: 18
# @Author   : Ranshi
# @File     : 123.py
from typing import List


class Solution:
    def findMagicIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] == i:
                return i
        return -1


if __name__ == "__main__":
    s = Solution()
    print(s.findMagicIndex(nums=[1, 2, 3, 4, 5]))
