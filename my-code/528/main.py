# -*- coding: UTF-8 -*-
# @Time     : 2021/08/30 07:54
# @Author   : Ranshi
# @File     : 123.py

from typing import List
import random
import bisect


class Solution:
    def __init__(self, w: List[int]):
        for i in range(1, len(w)):
            w[i] += w[i - 1]
        self.lst = w
        self.len = w[-1]

    def pickIndex(self) -> int:
        return bisect.bisect_right(self.lst, random.random() * self.len)


if __name__ == "__main__":
    s = Solution([1, 2, 4, 5])
    print(s.pickIndex())
