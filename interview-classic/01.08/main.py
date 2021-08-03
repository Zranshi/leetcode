# -*- coding:utf-8 -*-
# @Time     : 2021/6/27 22: 02
# @Author   : Ranshi
# @File     : 面试题 01.08. 零矩阵.py
from typing import List, Set


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        x_set: Set[int] = set()
        y_set: Set[int] = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    x_set.add(i)
                    y_set.add(j)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in x_set or j in y_set:
                    matrix[i][j] = 0


if __name__ == '__main__':
    s = Solution()
    print(s.setZeroes([
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]))
