# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 11
# @Author   : Ranshi
# @File     : 643. 子数组最大平均数 I.py
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        idx, length = 0, len(nums)
        ans = res = sum(nums[: idx + k])
        while idx + k < length:
            ans = ans - nums[idx] + nums[idx + k]
            res = max(ans, res)
            idx += 1
        return res / k


if __name__ == "__main__":
    s = Solution()
    print(s.findMaxAverage([1, 12, -5, -6, 50, 3], k=4))
