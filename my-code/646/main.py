# -*- coding: UTF-8 -*-
# @Time     : 2022/09/03 22:42
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 646. 最长数对链


from math import inf


class Solution:
    def findLongestChain(self, pairs: list[list[int]]) -> int:
        cur, res = -inf, 0
        for x, y in sorted(pairs, key=lambda x: x[1]):
            if cur < x:
                cur = y
                res += 1
        return res


if __name__ == "__main__":
    print(Solution().findLongestChain([[1, 2], [2, 3], [3, 4]]))
