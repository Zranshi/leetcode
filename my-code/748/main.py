#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/12/10 08:21
# @Author   : Ranshi
# @File     : 123.py
# @Doc      : 748. 最短补全词
from collections import Counter


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:
        cnt = Counter(ch.lower() for ch in licensePlate if ch.isalpha())
        return min((word for word in words if not cnt - Counter(word)), key=len)


if __name__ == "__main__":
    print(
        Solution().shortestCompletingWord(
            licensePlate="1s3 PSt", words=["step", "steps", "stripe", "stepple"]
        )
    )
