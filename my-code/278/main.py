# -*- coding: UTF-8 -*-
# @Time     : 2021/08/26 17:40
# @Author   : Ranshi
# @File     : 123.py


class Solution:
    def firstBadVersion(self, n: int) -> int:
        le, ri = 0, n
        while le < ri:
            idx = (le + ri) // 2
            if isBadVersion(idx):
                ri = idx
            else:
                le = idx + 1
        return le
