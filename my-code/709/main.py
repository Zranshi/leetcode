#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/12/12 09:29
# @Author   : Ranshi
# @File     : 123.py
# @Doc      : 709. 转换成小写字母
class Solution:
    def toLowerCase(self, s: str) -> str:
        res = [""] * len(s)
        for i, v in enumerate(s):
            if 65 <= ord(v) <= 90:
                res[i] = chr(ord(v) + 32)
            else:
                res[i] = v
        return "".join(res)


if __name__ == "__main__":
    print(Solution().toLowerCase(s="Hello"))
