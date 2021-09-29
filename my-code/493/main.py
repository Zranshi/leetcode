# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 10
# @Author   : Ranshi
# @File     : 493. 翻转对.py
import bisect
from typing import List


class Solution:
    # 暴力，过不了...
    def reversePairs1(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[i] > 2 * nums[j]:
                    res += 1
        return res

    # 调用库函数的二分查找
    def reversePairs2(self, nums: List[int]) -> int:
        ri, res, n = [], 0, len(nums)
        for i in reversed(range(n)):
            res += bisect.bisect_left(ri, nums[i])
            bisect.insort(ri, 2 * nums[i])
        return res

    # 归并算法改
    def reversePairs(self, nums: List[int]) -> int:
        pass


if __name__ == "__main__":
    s = Solution()
    print(s.reversePairs([2, 4, 3, 5, 1]))
