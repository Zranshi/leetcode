#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/12/01 08:51
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 1446. 连续字符
class Solution:
    def maxPower(self, s: str) -> int:
        if len(s) == 0:
            return 0
        res = 1
        idx = 1
        i = 1
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                idx, res = 1, max(idx, res)
            if s[i] == s[i - 1]:
                idx += 1
        else:
            res = max(idx, res)
        return res


if __name__ == "__main__":
    print(Solution().maxPower(s=""))
