#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/10/14 07:21
# @Author   : Ranshi
# @File     : 123.py
# @Doc      : 剑指 Offer II 069. 山峰数组的顶部
from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1
        while left != right:
            mid = (left + right) // 2
            if arr[mid - 1] < arr[mid] and arr[mid + 1] < arr[mid]:
                return mid
            elif arr[mid - 1] > arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return left


if __name__ == "__main__":
    print(Solution().peakIndexInMountainArray(arr=[24, 69, 100, 99, 79, 78, 67, 36, 26, 19]))
