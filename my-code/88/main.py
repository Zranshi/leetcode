# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 17: 57
# @Author   : Ranshi
# @File     : 88. 合并两个有序数组.py
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int):
        idx, idx1, idx2 = 1, 1, 1
        while idx1 <= m and idx2 <= n:
            if nums1[m - idx1] > nums2[n - idx2]:
                nums1[m + n - idx] = nums1[m - idx1]
                idx1 += 1
            else:
                nums1[m + n - idx] = nums2[n - idx2]
                idx2 += 1
            idx += 1
        if idx2 <= n:
            while idx2 <= n:
                nums1[m + n - idx] = nums2[n - idx2]
                idx += 1
                idx2 += 1
        return


if __name__ == '__main__':
    s = Solution()
    print(s.merge(nums1=[0], m=0, nums2=[1], n=1))
