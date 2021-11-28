#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/11/17 08:25
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 318. 最大单词长度乘积
from collections import defaultdict
from functools import reduce
from itertools import product
from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        masks = defaultdict(int)
        for word in words:
            mask = reduce(lambda a, b: a | (1 << (ord(b) - ord("a"))), word, 0)
            masks[mask] = max(masks[mask], len(word))
        return max(
            (masks[x] * masks[y] for x, y in product(masks, repeat=2) if x & y == 0), default=0
        )


if __name__ == "__main__":
    print(Solution().maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]))
