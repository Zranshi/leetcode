# -*- coding: UTF-8 -*-
# @Time     : 2023/02/04 00:21
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 剑指 Offer II 080. 含有 k 个元素的组合
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        tmp = []
        res = []

        def dfs(cur):
            if len(tmp) == k:
                res.append(tmp[:])
                return
            if cur > n:
                return
            tmp.append(cur)
            dfs(cur + 1)
            tmp.pop()
            dfs(cur + 1)
            return

        dfs(1)
        return res


print(Solution().combine(n=4, k=2))
