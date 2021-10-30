# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 17: 53
# @Author   : Ranshi
# @File     : 74. 搜索二维矩阵.py
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        a = []
        for x in matrix:
            a += x
        left, right = 0, len(a)
        while left < right:
            mid = (left + right) // 2
            if a[mid] == target:
                return True
            else:
                if target > a[mid]:
                    left = mid + 1
                else:
                    right = mid
        return False


if __name__ == "__main__":
    s = Solution()
    print(s.searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], target=14))
