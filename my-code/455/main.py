# -*- coding: UTF-8 -*-
# @Time     : 2021/08/23 10:12 下午
# @Author   : Ranshi
# @File     : main.py
from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        res = 0
        idx_child = 0
        idx_candy = 0
        while idx_child < len(g) and idx_candy < len(s):
            if g[idx_child] <= s[idx_candy]:
                res += 1
                idx_candy, idx_child = idx_candy + 1, idx_child + 1
            else:
                idx_candy += 1
        return res


if __name__ == "__main__":
    print(Solution().findContentChildren(g=[1, 2, 3], s=[1, 1]))
