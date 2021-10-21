#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/10/21 11:37
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 剑指 Offer 38. 字符串的排列
from typing import List


class Solution:
    def permutation(self, s: str) -> List[str]:
        lst = list(s)
        res = set()

        def dfs(arr: list, le: int, ri: int):
            if le == ri:
                res.add("".join(arr))
            else:
                i = le
                for num in range(le, ri):
                    arr[num], arr[i] = arr[i], arr[num]
                    dfs(arr, le + 1, ri)
                    arr[num], arr[i] = arr[i], arr[num]

        dfs(lst, 0, len(lst))
        return list(res)


if __name__ == "__main__":
    print(Solution().permutation(s="abc"))
