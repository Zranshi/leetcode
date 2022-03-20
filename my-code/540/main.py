# -*- coding: UTF-8 -*-
# @Time     : 2022/02/14 21:16
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 540. 有序数组中的单一元素
class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            mid -= mid & 1
            if nums[mid] == nums[mid + 1]:
                low = mid + 2
            else:
                high = mid
        return nums[low]


if __name__ == "__main__":
    print(Solution().singleNonDuplicate(nums=[3, 3, 7, 7, 10, 11, 11]))
