# -*- coding: UTF-8 -*-
# @Time     : 2021/09/15 08:15
# @Author   : Ranshi
# @File     : main.py
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)

        def get(i: int) -> int:
            if i == -1 or i == n:
                return float("-inf")
            return nums[i]

        left, right, ans = 0, n - 1, -1
        while left <= right:
            mid = (left + right) // 2
            if get(mid - 1) < get(mid) > get(mid + 1):
                ans = mid
                break
            if get(mid) < get(mid + 1):
                left = mid + 1
            else:
                right = mid - 1

        return ans


if __name__ == "__main__":
    print(Solution().findPeakElement(nums=[1, 2, 3, 1]))
