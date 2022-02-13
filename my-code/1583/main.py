# coding: utf-8
# @Time     : 2021/08/14 09:01
# @Author   : Ranshi
# @File     : 123.py

from typing import List


class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        f_ships = [[-1] * n for _ in range(n)]
        for idx, v in enumerate(preferences):
            for i in range(len(v)):
                f_ships[idx][v[i]] = i
        match = [0] * n
        for x, y in pairs:
            match[x] = y
            match[y] = x
        res = 0
        for x in range(n):
            y = match[x]
            idx = f_ships[x][y]
            for i in range(idx):
                u = preferences[x][i]
                v = match[u]
                if f_ships[u][x] < f_ships[u][v]:
                    res += 1
                    break
        return res


if __name__ == "__main__":
    print(
        Solution().unhappyFriends(
            n=4,
            preferences=[
                [1, 2, 3],
                [3, 2, 0],
                [3, 1, 0],
                [1, 2, 0],
            ],
            pairs=[
                [0, 1],
                [2, 3],
            ],
        )
    )
