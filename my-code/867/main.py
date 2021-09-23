# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 15
# @Author   : Ranshi
# @File     : 867. 转置矩阵.py
from typing import List


class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        return [list(x) for x in zip(*A)]


if __name__ == "__main__":
    s = Solution()
    print(s.transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
