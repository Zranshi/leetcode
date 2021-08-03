# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 11
# @Author   : Ranshi
# @File     : 587. 安装栅栏.py
from typing import List


class Solution:
    def outerTrees(self, points: List[List[int]]):
        n = len(points)
        if n < 3:
            return points
        points.sort(key=lambda x: (x[0], x[1]))

        def cross(a, b, c):
            return (b[0] - a[0]) * \
                   (c[1] - b[1]) - (b[1] - a[1]) * (c[0] - b[0])

        low = []
        for p in points:
            while len(low) > 1 and cross(low[-2], low[-1], p) < 0:
                low.pop()
            low.append((p[0], p[1]))
        up = []
        for p in reversed(points):
            while len(up) > 1 and cross(up[-2], up[-1], p) < 0:
                up.pop()
            up.append((p[0], p[1]))
        return list(set(low[:-1] + up[:-1]))
