# -*- coding: UTF-8 -*-
# @Time     : 2021/08/23 22:04
# @Author   : Ranshi
# @File     : main.py

from typing import List


class Solution:

    def minMoves(self, nums: List[int]) -> int:
        _min = nums[0]
        res = 0
        for i in range(len(nums)):
            _min = min(_min, nums[i])
        for i in range(len(nums)):
            res += nums[i] - _min
        return res


if __name__ == '__main__':
    print(Solution().minMoves([1, 2, 3]))
