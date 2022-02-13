#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/12/12 21:40
# @Author   : Ranshi
# @File     : 123.py
# @Doc      : 833. 字符串中的查找与替换
class Solution:
    def findReplaceString(
        self, S: str, indexes: list[int], sources: list[str], targets: list[str]
    ) -> str:
        N, chs = len(indexes), list(S)
        for i, S, t in sorted(
            [(indexes[i], sources[i], targets[i]) for i in range(N)], reverse=True
        ):
            if chs[i : i + len(S)] == list(S):
                chs[i : i + len(S)] = list(t)
        return "".join(chs)


if __name__ == "__main__":
    print(
        Solution().findReplaceString(
            S="abcd", indexes=[0, 2], sources=["a", "cd"], targets=["eee", "ffff"]
        )
    )
