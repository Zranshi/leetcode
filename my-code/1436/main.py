# -*- coding: UTF-8 -*-
# @Time     : 2021/10/01 00:11
# @Author   : Ranshi
# @File     : 123.py
from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        d = {}
        s = set()
        for start, end in paths:
            d[start] = end
            s.add(start)
            s.add(end)
        for key in s:
            if key not in d:
                return key
        return ""


if __name__ == "__main__":
    print(
        Solution().destCity(
            paths=[
                ["London", "New York"],
                ["New York", "Lima"],
                ["Lima", "Sao Paulo"],
            ]
        )
    )
