# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 14
# @Author   : Ranshi
# @File     : 766. 托普利茨矩阵.py
from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(len(matrix) - 1):
            if matrix[i][:-1] != matrix[i + 1][1:]:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isToeplitzMatrix(
        matrix=[[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]))
