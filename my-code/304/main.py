# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 07
# @Author   : Ranshi
# @File     : 304. 二维区域和检索 - 矩阵不可变.py
from typing import List


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), (len(matrix[0]) if matrix else 0)
        self.m = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                self.m[i + 1][j + 1] = (
                    self.m[i][j + 1]
                    + self.m[i + 1][j]
                    - self.m[i][j]
                    + matrix[i][j]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.m[row2 + 1][col2 + 1]
            - self.m[row1][col2 + 1]
            - self.m[row2 + 1][col1]
            + self.m[row1][col1]
        )


if __name__ == "__main__":
    n = NumMatrix(
        matrix=[
            [3, 0, 1, 4, 2],
            [5, 6, 3, 2, 1],
            [1, 2, 0, 1, 5],
            [4, 1, 0, 1, 7],
            [1, 0, 3, 0, 5],
        ]
    )
    print(n.sumRegion(2, 1, 4, 3))
