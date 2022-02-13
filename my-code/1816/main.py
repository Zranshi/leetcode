#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/12/06 09:02
# @Author   : Ranshi
# @File     : 123.py
# @Doc      : 1816. 截断句子
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return " ".join(s.split(" ")[:k])


if __name__ == "__main__":
    print(Solution().truncateSentence(s="Hello how are you Contestant", k=4))
