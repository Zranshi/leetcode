#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/11/05 08:12
# @Author   : Ranshi
# @File     : 123.py
# @Doc      : 1218. 最长定差子序列
from collections import defaultdict


class Solution:
    def longestSubsequence(self, arr: list[int], difference: int) -> int:
        dp = defaultdict(int)
        for v in arr:
            dp[v] = dp[v - difference] + 1
        return max(dp.values())


if __name__ == "__main__":
    print(Solution().longestSubsequence(arr=[1, 2, 3, 4], difference=1))
