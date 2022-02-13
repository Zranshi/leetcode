# -*- coding: UTF-8 -*-
# @Time     : 2021/08/23 10:06
# @Author   : Ranshi
# @File     : 123.py

from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n, num, vis = len(rooms), 0, set()

        def dfs(x: int):
            vis.add(x)
            nonlocal num
            num += 1
            for it in rooms[x]:
                if it not in vis:
                    dfs(it)

        dfs(0)
        return num == n


if __name__ == "__main__":
    print(Solution().canVisitAllRooms([[1], [2], [3], []]))
