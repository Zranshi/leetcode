# -*- coding: UTF-8 -*-
# @Time     : 2021/08/25 08:30
# @Author   : Ranshi
# @File     : main.py

from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        from math import sqrt

        res = []
        for i, v in enumerate(points):
            res.append((sqrt(v[0] ** 2 + v[1] ** 2), i))
        heapq.heapify(res)
        return [points[heapq.heappop(res)[1]] for _ in range(k)]


if __name__ == "__main__":
    print(Solution().kClosest(points=[[1, 3], [-2, 2]], k=1))
