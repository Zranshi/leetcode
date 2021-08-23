# -*- coding: UTF-8 -*-
# @Time     : 2021/08/21 22:39
# @Author   : Ranshi
# @File     : main.py

from typing import List


class Solution:

    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        nega_num, min_num, sum_num = 0, float('inf'), 0
        for item in matrix:
            for x in item:
                if x < 0:
                    nega_num += 1
                sum_num += abs(x)
                if min_num > abs(x):
                    min_num = abs(x)
        return int(sum_num if nega_num % 2 == 0 else sum_num - 2 * min_num)


if __name__ == '__main__':
    print(Solution().maxMatrixSum(matrix=[[1, 2, 3], [-1, -2, -3], [1, 2, 3]]))
