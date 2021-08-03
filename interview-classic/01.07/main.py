# -*- coding:utf-8 -*-
# @Time     : 2021/6/27 21: 38
# @Author   : Ranshi
# @File     : 面试题 01.07. 旋转矩阵.py
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        if n <= 1:
            return
        for i in range((n + 1) // 2):
            for j in range(n // 2):
                x, y = i, j
                idx = matrix[x][y]
                for _ in range(4):
                    x, y = y, n - x - 1
                    idx, matrix[x][y] = matrix[x][y], idx


if __name__ == '__main__':
    s = Solution()
    print(s.rotate([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]))
