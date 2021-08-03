# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 17
# @Author   : Ranshi
# @File     : 945. 使数组唯一的最小增量.py
from typing import List


class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        A.sort()
        res = 0
        for i in range(1, len(A)):
            if A[i] <= A[i - 1]:
                res += A[i - 1] + 1 - A[i]
                A[i] = A[i - 1] + 1
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.minIncrementForUnique([3, 2, 1, 2, 1, 7]))
