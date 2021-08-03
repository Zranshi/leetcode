# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 17: 52
# @Author   : Ranshi
# @File     : 59. 螺旋矩阵 II.py
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        dirs = [(0, 1), [1, 0], (0, -1), (-1, 0)]
        matrix = [[0] * n for _ in range(n)]
        row, col, dirIdx = 0, 0, 0
        for i in range(n * n):
            matrix[row][col] = i + 1
            dx, dy = dirs[dirIdx]
            r, c = row + dx, col + dy
            if r < 0 or r >= n or c < 0 or c >= n or matrix[r][c] > 0:
                dirIdx = (dirIdx + 1) % 4  # 顺时针旋转至下一个方向
                dx, dy = dirs[dirIdx]
            row, col = row + dx, col + dy

        return matrix


if __name__ == '__main__':
    s = Solution()
    print(s.generateMatrix(n=3))
