# -*- coding:utf-8 -*-
# @Time     : 2021/5/19 20:22
# @Author   : Ranshi
# @File     : 912. 排序数组.py
from typing import List


class Solution:
    def merge_sort(self, nums, low, high):
        if low == high:
            return
        mid = (low + high) // 2
        self.merge_sort(nums, low, mid)
        self.merge_sort(nums, mid + 1, high)
        tmp = []
        i, j = low, mid + 1
        while i <= mid or j <= high:
            if i > mid or (j <= high and nums[j] < nums[i]):
                tmp.append(nums[j])
                j += 1
            else:
                tmp.append(nums[i])
                i += 1
        nums[low: high + 1] = tmp

    def sortArray(self, nums: List[int]) -> List[int]:
        self.merge_sort(nums, 0, len(nums) - 1)
        return nums


if __name__ == '__main__':
    s = Solution()
    print(s.sortArray(nums=[5, 2, 3, 1]))
