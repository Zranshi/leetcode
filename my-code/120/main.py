# -*- coding: UTF-8 -*-
# @Time     : 2021/09/06 08:17
# @Author   : Ranshi
# @File     : 123.py
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        f = [[0] * n for _ in range(2)]
        f[0][0] = triangle[0][0]

        for i in range(1, n):
            curr, prev = i % 2, 1 - i % 2
            f[curr][0] = f[prev][0] + triangle[i][0]
            for j in range(1, i):
                f[curr][j] = min(f[prev][j - 1], f[prev][j]) + triangle[i][j]
            f[curr][i] = f[prev][i - 1] + triangle[i][i]

        return min(f[(n - 1) % 2])


if __name__ == "__main__":
    print(Solution().minimumTotal(triangle=[[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
