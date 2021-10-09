# coding: utf-8
# @Time     : 2021/08/12 16:49
# @Author   : Ranshi
# @File     : main.py

from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        import heapq

        nums = [-item for item in set(nums)]
        heapq.heapify(nums)
        if len(nums) >= 3:
            for _ in range(2):
                heapq.heappop(nums)

        return -nums[0]


if __name__ == "__main__":
    print(
        Solution().thirdMax(
            [
                1,
                123,
                1,
                412,
                3,
                12,
                4,
                231,
                5,
                32,
                123,
                324,
                5,
                23,
                412,
                3,
                12,
                3,
            ]
        )
    )
