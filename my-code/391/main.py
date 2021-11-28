#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/11/16 08:44
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 391. 完美矩形
from typing import DefaultDict, List


class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        area, minX, minY, maxX, maxY = (
            0,
            rectangles[0][0],
            rectangles[0][1],
            rectangles[0][2],
            rectangles[0][3],
        )
        cnt = DefaultDict(int)
        for rect in rectangles:
            x, y, a, b = rect[0], rect[1], rect[2], rect[3]
            area += (a - x) * (b - y)

            minX = min(minX, x)
            minY = min(minY, y)
            maxX = max(maxX, a)
            maxY = max(maxY, b)

            cnt[(x, y)] += 1
            cnt[(x, b)] += 1
            cnt[(a, y)] += 1
            cnt[(a, b)] += 1

        if (
            area != (maxX - minX) * (maxY - minY)
            or cnt[(minX, minY)] != 1
            or cnt[(minX, maxY)] != 1
            or cnt[(maxX, minY)] != 1
            or cnt[(maxX, maxY)] != 1
        ):
            return False

        del cnt[(minX, minY)], cnt[(minX, maxY)], cnt[(maxX, minY)], cnt[(maxX, maxY)]

        return all(c in [2, 4] for c in cnt.values())


if __name__ == "__main__":
    print(
        Solution().isRectangleCover(
            rectangles=[[1, 1, 3, 3], [3, 1, 4, 2], [3, 2, 4, 4], [1, 3, 2, 4], [2, 3, 3, 4]]
        )
    )
