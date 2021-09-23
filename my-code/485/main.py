# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 10
# @Author   : Ranshi
# @File     : 485. 最大连续1的个数.py
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        idx, res = 0, 0
        for i in range(len(nums)):
            if nums[i] == 1:
                idx += 1
            else:
                res = max(res, idx)
                idx = 0
        return max(idx, res)


if __name__ == "__main__":
    s = Solution()
    print(s.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
