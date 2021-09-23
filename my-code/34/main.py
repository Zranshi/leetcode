# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 17: 51
# @Author   : Ranshi
# @File     : 34. 在排序数组中查找元素的第一个和最后一个位置.py
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low, high, mid = 0, len(nums) - 1, 0
        while low <= high:
            mid = int(low + (high - low) / 2)
            if nums[mid] == target:
                break
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        if low <= high:
            i, _min = mid, mid
            while i > 0:
                if nums[i - 1] == target:
                    i -= 1
                else:
                    break
            i, _min = mid, i
            while i < len(nums) - 1:
                if nums[i + 1] == target:
                    i += 1
                else:
                    break
            return [_min, i]
        else:
            return [-1, -1]


if __name__ == "__main__":
    s = Solution()
    print(s.searchRange(nums=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], target=10))
