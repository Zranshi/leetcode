# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 09
# @Author   : Ranshi
# @File     : 378. 有序矩阵中第K小的元素.py
from typing import List


class Solution:
    # 函数调用法
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        a = []
        for i in matrix:
            for num in i:
                a.append(num)
        a.sort()
        return a[k - 1]


if __name__ == "__main__":
    s = Solution()
    print(s.kthSmallest(matrix=[[1, 5, 9], [10, 11, 13], [12, 13, 15]], k=1))
