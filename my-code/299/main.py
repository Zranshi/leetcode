#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/11/08 15:57
# @Author   : Ranshi
# @File     : 123.py
# @Doc      : 299. 猜数字游戏
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cntS, cntG = [0] * 10, [0] * 10
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                cntS[int(s)] += 1
                cntG[int(g)] += 1
        cows = sum(min(s, g) for s, g in zip(cntS, cntG))
        return f"{bulls}A{cows}B"


if __name__ == "__main__":
    print(Solution().getHint(secret="1807", guess="7810"))
