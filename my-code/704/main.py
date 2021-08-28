# -*- coding: UTF-8 -*-
# @Time     : 2021/08/26 17:33
# @Author   : Ranshi
# @File     : main.py

from typing import List


class Solution:

    def search(self, nums: List[int], target: int) -> int:
        le, ri = 0, len(nums) - 1
        while le <= ri:
            mid = (le + ri) // 2
            if nums[mid] < target:
                le = mid + 1
            elif nums[mid] > target:
                ri = mid - 1
            else:
                return mid
        return -1


if __name__ == '__main__':
    print(Solution().search(nums=[-1, 0, 3, 5, 9, 12], target=9))
