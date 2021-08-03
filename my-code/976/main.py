# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 17
# @Author   : Ranshi
# @File     : 976. 三角形的最大周长.py
from typing import List


class Solution:
    # 贪心
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort(reverse=True)
        if len(A) < 3:
            return 0
        for i in range(2, len(A)):
            a, b, c = A[i], A[i - 1], A[i - 2]
            if c < b + a:
                return a + b + c
        return 0


if __name__ == "__main__":
    s = Solution()
    print(s.largestPerimeter([1, 2, 1]))
