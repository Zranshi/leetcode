#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/12/07 09:35
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 1034. 边界着色
from collections import deque


class Solution:
    def colorBorder(self, grid: list[list[int]], row: int, col: int, color: int) -> list[list[int]]:
        dq = deque([(row, col)])
        point_set: set[tuple[int, int]] = set()
        target_color = grid[row][col]
        boundary_list = []
        while dq:
            idx_row, idx_col = dq.pop()
            point_set.add((idx_row, idx_col))
            is_boundary = False
            for move_row, move_col in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                next_row, next_col = idx_row + move_row, idx_col + move_col
                if (
                    0 <= next_row < len(grid)
                    and 0 <= next_col < len(grid[0])
                    and grid[next_row][next_col] == target_color
                ):
                    if (next_row, next_col) not in point_set:
                        dq.appendleft((next_row, next_col))
                else:
                    is_boundary = True
                if is_boundary:
                    boundary_list.append((idx_row, idx_col))
        for b_row, b_col in boundary_list:
            grid[b_row][b_col] = color
        return grid


if __name__ == "__main__":
    print(
        Solution().colorBorder(
            grid=[[1, 2, 1, 2, 1, 2], [2, 2, 2, 2, 1, 2], [1, 2, 2, 2, 1, 2]], row=1, col=3, color=1
        )
    )
