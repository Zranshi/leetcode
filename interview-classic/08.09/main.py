# -*- coding:utf-8 -*-
# @Time     : 2021/7/20 14: 06
# @Author   : Ranshi
# @File     : main.py
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(d: int, height: int, idx=None):
            if idx is None:
                idx = list()
            if height == 0:
                res.append("".join(idx))
            else:
                if d == 0 or d < height:
                    idx.append("(")
                    dfs(d + 1, height - 1, idx)
                    idx.pop()
                if d > 0:
                    idx.append(")")
                    dfs(d - 1, height - 1, idx)
                    idx.pop()

        dfs(d=0, height=2 * n, idx=[])
        return res


if __name__ == "__main__":
    print(Solution().generateParenthesis(n=3))
