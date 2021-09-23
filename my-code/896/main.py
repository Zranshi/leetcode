# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 16
# @Author   : Ranshi
# @File     : 896. 单调数列.py
class Solution:
    def isMonotonic(self, A):
        B = sorted(A)
        C = B[:]
        C.reverse()
        return A == B or C == A


if __name__ == "__main__":
    s = Solution()
    print(s.isMonotonic([1, 2, 2, 3]))
