# -*- coding:utf-8 -*-
# @Time     : 2021/08/05 00:47
# @Author   : Ranshi
# @File     : main.py

from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        color = [0] * len(graph)

        def safe(x: int) -> bool:
            if color[x] > 0:
                return color[x] == 2
            color[x] = 1
            for y in graph[x]:
                if not safe(y):
                    return False
            color[x] = 2
            return True

        return [i for i in range(len(graph)) if safe(i)]


if __name__ == "__main__":
    print(
        Solution().eventualSafeNodes(
            graph=[[1, 2], [2, 3], [5], [0], [5], [], []]
        )
    )
