# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 15
# @Author   : Ranshi
# @File     : 832. 翻转图像.py
from typing import List


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        return [[j ^ 1 for j in item[::-1]] for item in A]


if __name__ == "__main__":
    s = Solution()
    print(s.flipAndInvertImage([[1, 1, 0], [1, 0, 1], [0, 0, 0]]))
