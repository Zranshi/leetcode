# -*- coding: UTF-8 -*-
# @Time     : 2021/08/28 09:08
# @Author   : Ranshi
# @File     : main.py

from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        res = []
        idx1, idx2 = 0, 0
        while idx1 < len(nums1) and idx2 < len(nums2):
            if nums1[idx1] == nums2[idx2]:
                res.append(nums1[idx1])
            elif nums1[idx1] < nums2[idx2]:
                idx2 -= 1
            else:
                idx1 -= 1
            idx1, idx2 = idx1 + 1, idx2 + 1
        return res


if __name__ == '__main__':
    print(Solution().intersect(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]))
