# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 17: 51
# @Author   : Ranshi
# @File     : 34. 在排序数组中查找元素的第一个和最后一个位置.py
class Solution:
    def binarySearch(self, nums: list[int], target: int, lower: bool):
        left, right = 0, len(nums) - 1
        ans = len(nums)
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target or (lower and nums[mid] >= target):
                right = mid - 1
                ans = mid
            else:
                left = mid + 1
        return ans

    def searchRange(self, nums: list[int], target: int) -> list[int]:
        left_idx = self.binarySearch(nums, target, True)
        right_idx = self.binarySearch(nums, target, False) - 1
        if (
            left_idx < right_idx
            and right_idx < len(nums)
            and nums[left_idx] == target
            and nums[right_idx] == target
        ):
            return [left_idx, right_idx]
        return [-1, -1]


if __name__ == "__main__":
    print(
        Solution().searchRange(nums=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], target=10)
    )
