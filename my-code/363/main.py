# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 08
# @Author   : Ranshi
# @File     : 363. 矩形区域不超过 K 的最大数值和.py
from typing import List


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        row, col = len(matrix) + 1, len(matrix[0]) + 1
        pre_sum = [[0 for _ in range(col)] for _ in range(row)]
        for i in range(1, row):
            for j in range(1, col):
                pre_sum[i][j] = (
                    pre_sum[i - 1][j]
                    + pre_sum[i][j - 1]
                    - pre_sum[i - 1][j - 1]
                    + matrix[i - 1][j - 1]
                )

        _max = -float("inf")
        for i in range(1, row):
            for j in range(1, col):
                for m in range(0, i):
                    for n in range(0, j):
                        item = (
                            pre_sum[i][j]
                            + pre_sum[m][n]
                            - pre_sum[i][n]
                            - pre_sum[m][j]
                        )
                        if item <= k:
                            _max = max(_max, item)
        return _max


if __name__ == "__main__":
    s = Solution()
    print(s.maxSumSubmatrix(matrix=[[2, 2, -1]], k=3))
