# -*- coding: UTF-8 -*-
# @Time     : 2021/09/30 19:33
# @Author   : Ranshi
# @File     : 123.py
from typing import List


class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        dp = [[0 for _ in range(len(grid[0]) + 1)] for _ in range(len(grid) + 1)]
        for i in range(1, len(grid) + 1):
            for j in range(1, len(grid[0]) + 1):
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j]) + grid[i - 1][j - 1]
        return dp[len(grid)][len(grid[0])]


if __name__ == "__main__":
    print(Solution().maxValue([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
