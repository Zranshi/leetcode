# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 15
# @Author   : Ranshi
# @File     : 861. 翻转矩阵后的得分.py
from typing import List


class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        n, m = len(A), len(A[0])
        res = n
        for i in range(1, m):
            res <<= 1
            s = sum(A[j][i] ^ A[j][0] for j in range(n))
            res += max(s, n - s)
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.matrixScore([
        [0, 0, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 0]
    ]))
