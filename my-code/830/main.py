# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 14
# @Author   : Ranshi
# @File     : 830. 较大分组的位置.py
from typing import List


class Solution:
    def largeGroupPositions1(self, s: str) -> List[List[int]]:
        res = []
        s = s[:] + '$'
        length = 1
        for i, x in enumerate(s):
            if x != s[i - 1]:
                if length >= 3:
                    res.append([i - length, i - 1])
                length = 1
            else:
                length += 1
        return res

    def largeGroupPositions(self, s: str) -> List[List[int]]:
        ret = list()
        n, num = len(s), 1

        for i in range(n):
            if i == n - 1 or s[i] != s[i + 1]:
                if num >= 3:
                    ret.append([i - num + 1, i])
                num = 1
            else:
                num += 1

        return ret


if __name__ == "__main__":
    s = Solution()
    print(s.largeGroupPositions1(s="aaaabcdddeeeeaabbbcdddd"))
