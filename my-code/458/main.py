#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/11/25 08:15
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 458. 可怜的小猪
class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        if buckets == 1:
            return 0
        combinations = [[0] * (buckets + 1) for _ in range(buckets + 1)]
        combinations[0][0] = 1
        iterations = minutesToTest // minutesToDie
        f = [[1] * (iterations + 1)] + [[1] + [0] * iterations for _ in range(buckets - 1)]
        for i in range(1, buckets):
            combinations[i][0] = 1
            for j in range(1, i):
                combinations[i][j] = combinations[i - 1][j - 1] + combinations[i - 1][j]
            combinations[i][i] = 1
            for j in range(1, iterations + 1):
                for k in range(i + 1):
                    f[i][j] += f[k][j - 1] * combinations[i][i - k]
            if f[i][iterations] >= buckets:
                return i
        return 0


if __name__ == "__main__":
    print(Solution().poorPigs(buckets=1000, minutesToDie=15, minutesToTest=60))
