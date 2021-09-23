# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 18
# @Author   : Ranshi
# @File     : 1004. 最大连续1的个数 III.py
from typing import List


class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        left, idx, right = 0, 0, 0
        for right in range(len(A)):
            idx += 1 - A[right]
            if idx > K:
                idx -= 1 - A[left]
                left += 1
        return right - left + 1


if __name__ == "__main__":
    s = Solution()
    print(s.longestOnes(A=[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], K=2))
