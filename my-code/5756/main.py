# -*- coding:utf-8 -*-
# @Time     : 2021/5/29 22:49
# @Author   : Ranshi
# @File     : 5756. 两个数组最小的异或值之和.py
from typing import List


class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        from collections import Counter
        c1, c2 = Counter(nums1), Counter(nums2)
        c1, c2 = c1 - c2, c2 - c1


if __name__ == '__main__':
    s = Solution()
    print(s.minimumXORSum(nums1=[1, 0, 3, 1], nums2=[5, 3, 4, 3]))
