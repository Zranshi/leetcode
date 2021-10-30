#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/10/29 22:52
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 面试题 10.09. 排序矩阵查找
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix:
            return False
        i, j = 0, len(matrix[0]) - 1
        while i < len(matrix) and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                i += 1
            else:
                j -= 1
        return False


if __name__ == "__main__":
    print(
        Solution().searchMatrix(
            [
                [1, 4, 7, 11, 15],
                [2, 5, 8, 12, 19],
                [3, 6, 9, 16, 22],
                [10, 13, 14, 17, 24],
                [18, 21, 23, 26, 30],
            ],
            target=20,
        )
    )
