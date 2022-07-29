# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 13
# @Author   : Ranshi
# @File     : 724. 寻找数组的中心索引.py
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        sumAll = sum(nums)
        sumHalf = 0
        for i in range(n):
            if sumHalf * 2 + nums[i] == sumAll:
                return i
            sumHalf += nums[i]
        return -1


if __name__ == "__main__":
    s = Solution()
    print(s.pivotIndex(nums=[-1, -1, -1, -1, -1, -1]))
