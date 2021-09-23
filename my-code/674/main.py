# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 12
# @Author   : Ranshi
# @File     : 674. 最长连续递增序列.py
from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        idx, res, pre = 0, 0, float("-inf")
        for x in nums:
            if x > pre:
                idx += 1
                res = max(res, idx)
            else:
                res = max(res, idx)
                idx = 1
            pre = x
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.findLengthOfLCIS(nums=[2, 2, 2, 2, 2]))
