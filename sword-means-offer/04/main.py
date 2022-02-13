# -*- coding: UTF-8 -*-
# @Time     : 2021/09/26 22:37
# @Author   : Ranshi
# @File     : 123.py
from typing import List


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        x, y = 0, len(matrix[0]) - 1
        while x < len(matrix) and y >= 0:
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] > target:
                y -= 1
            else:
                x += 1
        return False


if __name__ == "__main__":
    print(
        Solution().findNumberIn2DArray(
            [],
            20,
        )
    )
