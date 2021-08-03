# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 21
# @Author   : Ranshi
# @File     : 1579. 保证图可完全遍历.py
from typing import List


class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n
        self.n = n
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

    def connected(self, x: int, y: int) -> bool:
        x, y = self.findset(x), self.findset(y)
        return x == y


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        ufa, ufb = UnionFind(n), UnionFind(n)
        ans = 0
        for edge in edges:
            edge[1] -= 1
            edge[2] -= 1

        for t, u, v in edges:
            if t == 3:
                if not ufa.unite(u, v):
                    ans += 1
                else:
                    ufb.unite(u, v)
        for t, u, v in edges:
            if t == 1:
                if not ufa.unite(u, v):
                    ans += 1
            elif t == 2:
                if not ufb.unite(u, v):
                    ans += 1

        if ufa.setCount != 1 or ufb.setCount != 1:
            return -1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.maxNumEdgesToRemove(n=4, edges=[[3, 1, 2], [
        3, 2, 3], [1, 1, 3], [1, 2, 4], [1, 1, 2], [2, 3, 4]]))
