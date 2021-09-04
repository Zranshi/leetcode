# -*- coding:utf-8 -*-
# @Time     : 2021/7/1 09: 39
# @Author   : Ranshi
# @File     : main.py
from typing import List


class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        import numpy as np
        mapping = [[0] * n for _ in range(n)]
        for item in relation:
            mapping[item[0]][item[1]] = 1
        idx = np.array(mapping)
        arr = idx.copy()
        for i in range(k + 1):
            idx = idx.dot(arr)
        return idx[0][-1]


if __name__ == '__main__':
    s = Solution()
    print(s.numWays(n=5, relation=[[0, 2], [2, 1], [3, 4], [2, 3], [1, 4], [2, 0], [0, 4]], k=3))
