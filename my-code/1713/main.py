# -*- coding:utf-8 -*-
# @Time     : 2021/7/26 11:49
# @Author   : Ranshi
# @File     : main.py
from typing import List


class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        from bisect import bisect_left

        length = len(target)
        num_map = {x: i for i, x in enumerate(target)}
        arr, target, nums = (
            [num_map[x] for x in arr if x in num_map],
            [x for x in range(0, length)],
            [],
        )
        for idx in arr:
            i = bisect_left(nums, idx)
            if i < len(nums):
                nums[i] = idx
            else:
                nums.append(idx)
        return length - len(nums)


if __name__ == "__main__":
    print(
        Solution().minOperations(
            target=[6, 4, 8, 1, 3, 2], arr=[4, 7, 6, 2, 3, 8, 6, 1]
        )
    )
