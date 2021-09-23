# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 22
# @Author   : Ranshi
# @File     : 1734. 解码异或后的排列.py
from functools import reduce
from operator import xor
from typing import List


class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded) + 1
        total = reduce(xor, range(1, n + 1))
        odd = 0
        for i in range(1, n - 1, 2):
            odd ^= encoded[i]

        perm = [total ^ odd]
        for i in range(n - 1):
            perm.append(perm[-1] ^ encoded[i])
        return perm


if __name__ == "__main__":
    s = Solution()
    print(s.decode(encoded=[3, 1]))
