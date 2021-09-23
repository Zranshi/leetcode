# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 18
# @Author   : Ranshi
# @File     : 992. K 个不同整数的子数组.py
from collections import Counter
from typing import List


class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        res, left, length = 0, 0, len(A)
        c = Counter()
        for right in range(length):
            c[A[right]] += 1
            while len(c) >= K and left <= right:
                if len(c) == K:
                    tr = right
                    while tr < length and c[A[tr]] > 0:
                        res += 1
                        tr += 1
                if c[A[left]] == 1:
                    c.pop(A[left])
                else:
                    c[A[left]] -= 1
                left += 1
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.subarraysWithKDistinct(A=[1, 2, 1, 3, 4], K=3))
