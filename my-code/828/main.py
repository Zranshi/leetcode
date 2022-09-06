# -*- coding: UTF-8 -*-
# @Time     : 2022/09/06 22:25
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 828. 统计子串中的唯一字符
import collections


class Solution:
    def uniqueLetterString(self, s: str) -> int:
        idx = collections.defaultdict(list)
        for i, v in enumerate(s):
            idx[v].append(i)

        res = 0
        for arr in idx.values():
            arr = [-1] + arr + [len(s)]
            for i in range(1, len(arr) - 1):
                res += (arr[i] - arr[i - 1]) * (arr[i + 1] - arr[i])
        return res


if __name__ == "__main__":
    print(Solution().uniqueLetterString(s="LEETCODE"))
