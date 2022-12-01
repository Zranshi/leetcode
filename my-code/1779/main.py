# -*- coding: UTF-8 -*-
# @Time     : 2022/12/01 08:24
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 1779. 找到最近的有相同 X 或 Y 坐标的点


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: list[list[int]]) -> int:
        best, bestid = float("inf"), -1
        for i, (px, py) in enumerate(points):
            if x == px:
                if (dist := abs(y - py)) < best:
                    best = dist
                    bestid = i
            elif y == py:
                if (dist := abs(x - px)) < best:
                    best = dist
                    bestid = i

        return bestid


if __name__ == "__main__":
    print(
        Solution().nearestValidPoint(
            x=3, y=4, points=[[1, 2], [3, 1], [2, 3], [4, 4], [2, 4]]
        )
    )
