# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 17
# @Author   : Ranshi
# @File     : 959. 由斜杠划分区域.py
from typing import List


class UnionFind:
    def __init__(self, n):
        # 记录每个节点的父节点
        self.parent = list(range(n))
        # 记录每个连通图的节点个数
        self.size = [1] * n
        # 记录节点个数
        self.n = n

    def find(self, x: int) -> int:
        # 递归查找祖先节点
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def unite(self, x: int, y: int) -> bool:
        # 合并两个节点
        x, y = self.find(x), self.find(y)
        # 如果在同一个集合，则返回True，如果不是则返回False
        if x == y:
            return True
        if self.size[x] < self.size[y]:
            x, y = y, x
        # 打印出每次连接的数据
        print(f'父节点: {x}, 子节点: {y}')
        self.parent[y] = x
        self.size[x] += self.size[y]
        return False


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        size = len(grid)  # 获取边长
        # 格点数=(边长+1)*(边长+1)，所有格点初始化为指向自己
        V = {(i, j): (i, j) for j in range(size + 1) for i in range(size + 1)}
        for i in range(size + 1):  # 边框的格点是全部连接的，因此初始化为同一个集合
            V[i, 0], V[0, i], V[size, i], V[i, size] = (
                                                           0, 0), (0, 0), (0, 0), (0, 0)

        # 获取坐标c的格点的集合标记，用两点集合标记相同来表示两点相连
        def find(c):
            while V[c] != c:
                c = V[c]
            return c

        # 初始独立区域为一整个方框
        res = 1
        for i in range(size):
            for j in range(size):
                if grid[i][j] == '/':
                    # /会将点(i,j)右边和下边的点连起来
                    # 把结果存起来，避免merge时再查找一遍
                    t1 = find((i + 1, j))
                    t2 = find((i, j + 1))
                    # 如果两点已经相连了，那么新的/让它们形成了一个环，因此多出一个独立区域
                    if t1 == t2:
                        res += 1
                    else:  # 让它们相连
                        V[t1] = V[t2]  # 因为从上往下扫描，所以下面合入上面能减小整体的find长度
                elif grid[i][j] == '\\':
                    # \会将点(i,j)和它右下的点连起来，下略
                    t1 = find((i + 1, j + 1))
                    t2 = find((i, j))
                    if t1 == t2:
                        res += 1
                    else:
                        V[t1] = V[t2]
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.regionsBySlashes([
        "\\/",
        "/\\"
    ]))
