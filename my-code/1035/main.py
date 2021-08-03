# -*- coding:utf-8 -*-
# @Time     : 2021/5/21 07:44
# @Author   : Ranshi
# @File     : 1035. 不相交的线.py
from typing import List


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i, num1 in enumerate(nums1):
            for j, num2 in enumerate(nums2):
                if num1 == num2:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

        return dp[m][n]


if __name__ == '__main__':
    s = Solution()
    print(s.maxUncrossedLines(nums1=[1, 4, 2], nums2=[1, 2, 4]))
