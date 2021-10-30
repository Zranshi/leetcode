#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/10/22 08:21
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 剑指 Offer 51. 数组中的逆序对
class Solution:
    def mergeSort(self, nums, tmp, left, right):
        if left >= right:
            return 0

        mid = (left + right) // 2
        inv_count = self.mergeSort(nums, tmp, left, mid) + self.mergeSort(nums, tmp, mid + 1, right)
        i, j, pos = left, mid + 1, left
        while i <= mid and j <= right:
            if nums[i] <= nums[j]:
                tmp[pos] = nums[i]
                i += 1
                inv_count += j - (mid + 1)
            else:
                tmp[pos] = nums[j]
                j += 1
            pos += 1
        for k in range(i, mid + 1):
            tmp[pos] = nums[k]
            inv_count += j - (mid + 1)
            pos += 1
        for k in range(j, right + 1):
            tmp[pos] = nums[k]
            pos += 1
        nums[left : right + 1] = tmp[left : right + 1]
        return inv_count

    def reversePairs(self, nums: list[int]) -> int:
        n = len(nums)
        tmp = [0] * n
        return self.mergeSort(nums, tmp, 0, n - 1)


if __name__ == "__main__":
    print(Solution().reversePairs([7, 5, 6, 4]))
