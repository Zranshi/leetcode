# -*- coding: UTF-8 -*-
# @Time     : 2021/08/23 22:04
# @Author   : Ranshi
# @File     : main.py
from typing import List


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        _min = nums[0]
        for num_ in nums:
            _min = min(_min, num_)
        return sum(num - _min for num in nums)


if __name__ == "__main__":
    print(Solution().minMoves([1, 2, 3]))
