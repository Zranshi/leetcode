# -*- coding: UTF-8 -*-
# @Time     : 2022/09/04 22:47
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 1582. 二进制矩阵中的特殊位置


class Solution:
    def numSpecial(self, mat: list[list[int]]) -> int:
        r, c = len(mat), len(mat[0])
        row_1 = [sum(mat[i][j] for j in range(c)) for i in range(r)]
        col_1 = [sum(mat[j][i] for j in range(r)) for i in range(c)]

        return sum(mat[i][j] for i in range(r) for j in range(c) if row_1[i] == 1 and col_1[j] == 1)


if __name__ == "__main__":
    print(Solution().numSpecial(mat=[[1, 0, 0], [0, 0, 1], [1, 0, 0]]))
