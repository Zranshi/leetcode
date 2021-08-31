# -*- coding:utf-8 -*-
# @Time     : 2021/7/19 08: 32
# @Author   : Ranshi
# @File     : main.py
from typing import List


class Solution:

    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        le, res = 0, 0
        pre = [0]
        for x in nums:
            pre.append(pre[-1] + x)

        def idx_k() -> int:
            return nums[ri] * (ri - le + 1) - (pre[ri + 1] - pre[le])

        for ri in range(len(nums)):
            while idx_k() > k:
                le += 1
            res = max(res, (ri - le + 1))
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.maxFrequency(nums=[3, 9, 6], k=2))
