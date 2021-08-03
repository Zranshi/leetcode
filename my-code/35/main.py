# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 17: 51
# @Author   : Ranshi
# @File     : 35. 搜索插入位置.py
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left


if __name__ == '__main__':
    s = Solution()
    print(s.searchInsert([3, 3, 5, 6], 2))
