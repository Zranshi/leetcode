# -*- coding: UTF-8 -*-
# @Time     : 2021/08/25 08:14
# @Author   : Ranshi
# @File     : main.py

from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        """
        输出DAG从0到n-1结点的所有可能路径.

        Args:
            graph (List[List[int]]): DAG

        Returns:
            List[List[int]]: 路径
        """
        n = len(graph)
        res = []
        path = []

        def dfs(idx: int):
            path.append(idx)
            if idx == n - 1:
                res.append(path[:])
            else:
                for _next in graph[idx]:
                    dfs(_next)
            path.pop()

        dfs(0)
        return res


if __name__ == "__main__":
    print(Solution().allPathsSourceTarget(graph=[[1, 2], [3], [3], []]))
