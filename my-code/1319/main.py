# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 20
# @Author   : Ranshi
# @File     : 1319. 连通网络的操作次数.py
from typing import List


# 并查集模版
class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n
        self.n = n
        # 当前连通分量数目
        self.setCount = n

    def findset(self, x: int) -> int:
        if self.parent[x] == x:
            return x
        self.parent[x] = self.findset(self.parent[x])
        return self.parent[x]

    def unite(self, x: int, y: int) -> bool:
        x, y = self.findset(x), self.findset(y)
        if x == y:
            return False
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]
        self.setCount -= 1
        return True


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        length = len(connections)
        if length < n - 1:
            return -1
        uf = UnionFind(n)
        for x, y in connections:
            uf.unite(x, y)
        return uf.setCount - 1


if __name__ == "__main__":
    s = Solution()
    print(s.makeConnected(n=4, connections=[[0, 1], [0, 2], [1, 2]]))
