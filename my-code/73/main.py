# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 17: 53
# @Author   : Ranshi
# @File     : 73. 矩阵置零.py
from typing import List


class Solution:

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        a = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    a.append([i, j])

        def clean(a, b):
            for i in range(len(matrix)):
                matrix[i][b] = 0
            for i in range(len(matrix[0])):
                matrix[a][i] = 0

        for x in a:
            clean(x[0], x[1])


if __name__ == "__main__":
    s = Solution()
    s.setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]])
