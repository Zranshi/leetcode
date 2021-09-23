# -*- coding:utf-8 -*-
# @Time     : 2021/6/15 18: 58
# @Author   : Ranshi
# @File     : 852. 山脉数组的峰顶索引.py
from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        left, right, ans = 1, n - 2, 0

        while left <= right:
            mid = (left + right) // 2
            if arr[mid] > arr[mid + 1]:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.peakIndexInMountainArray(arr=[0, 2, 1, 0]))
