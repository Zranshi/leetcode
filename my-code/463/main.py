# -*- coding:utf-8 -*-
# @Time     : 2021/7/3 14: 56
# @Author   : Ranshi
# @File     : main.py
from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0
        row, col = len(grid), len(grid[0])
        for i, j in [(i, j) for i in range(row) for j in range(col)]:
            if grid[i][j] == 1:
                for path in {(1, 0), (-1, 0), (0, 1), (0, -1)}:
                    if (
                        not (0 <= i + path[0] < row and 0 <= j + path[1] < col)
                        or grid[i + path[0]][j + path[1]] == 0
                    ):
                        res += 1
        return res


if __name__ == "__main__":
    s = Solution()
    print(
        s.islandPerimeter(
            grid=[[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
        )
    )
