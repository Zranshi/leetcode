# -*- coding: UTF-8 -*-
# @Time     : 2021/08/21 22:50
# @Author   : Ranshi
# @File     : main.py

from typing import List


class Solution:

    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        from collections import defaultdict
        points = [float('inf') for _ in range(n)]
        idx = 0
        flag = True
        mapping = defaultdict(dict)
        for road in roads:
            mapping[road[0]][road[1]] = road[2]
            mapping[road[1]][road[0]] = road[2]
        while flag:
            flag = False
            next_node, cost = -1, float('inf')
            for _next in mapping[idx]:
                if points[_next] > points[idx] + mapping[idx][_next]:
                    points[_next] = points[idx] + mapping[idx][_next]
                    flag = True
                if cost > mapping[idx][_next]:
                    cost = mapping[idx][_next]
                    next_node = _next
            idx = next_node
        return 0


if __name__ == '__main__':
    print(Solution().countPaths(
        n=7,
        roads=[
            [0, 6, 7],
            [0, 1, 2],
            [1, 2, 3],
            [1, 3, 3],
            [6, 3, 3],
            [3, 5, 1],
            [6, 5, 1],
            [2, 5, 1],
            [0, 4, 5],
            [4, 6, 2],
        ],
    ))
