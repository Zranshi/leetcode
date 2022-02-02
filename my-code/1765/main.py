# -*- coding: UTF-8 -*-
# @Time     : 2022/01/29 11:10
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 1765. 地图中的最高点
from collections import deque


class Solution:
    def highestPeak(self, isWater: list[list[int]]) -> list[list[int]]:
        m, n = len(isWater), len(isWater[0])
        ans = [[water - 1 for water in row] for row in isWater]
        q = deque((i, j) for i, row in enumerate(isWater) for j, water in enumerate(row) if water)
        while q:
            i, j = q.popleft()
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < m and 0 <= y < n and ans[x][y] == -1:
                    ans[x][y] = ans[i][j] + 1
                    q.append((x, y))
        return ans


if __name__ == "__main__":
    print(Solution().highestPeak(isWater=[[0, 1], [0, 0]]))
