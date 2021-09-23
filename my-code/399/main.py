# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 09
# @Author   : Ranshi
# @File     : 399. 除法求值.py
from typing import List


class Solution:
    def calcEquation(
        self,
        equations: List[List[str]],
        values: List[float],
        queries: List[List[str]],
    ) -> List[float]:
        from collections import defaultdict

        # 创建图
        graph = defaultdict(dict)
        for (x, y), val in zip(equations, values):
            graph[x][y] = val
            graph[y][x] = 1 / val
        res = []
        for s, e in queries:
            visited = set()
            res.append(self.dfs(s, e, visited, graph))
        return res

    def dfs(self, start, end, visited, graph):
        visited.add(start)
        if start not in graph:
            return -1
        if start == end:
            return 1
        for w in graph[start]:
            if w == end:
                return graph[start][w]
            elif w not in visited:
                visited.add(w)
                v = self.dfs(w, end, visited, graph)
                if v != -1:
                    return graph[start][w] * v
                else:
                    pass
        return -1


if __name__ == "__main__":
    s = Solution()
    print(
        s.calcEquation(
            equations=[["a", "b"], ["b", "c"]],
            values=[2.0, 3.0],
            queries=[
                ["a", "c"],
                ["b", "a"],
                ["a", "e"],
                ["a", "a"],
                ["x", "x"],
            ],
        )
    )
