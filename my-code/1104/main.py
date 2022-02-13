# -*- coding:utf-8 -*-
# @Time     : 2021/07/29 00:09
# @Author   : Ranshi
# @File     : 123.py

from typing import List


class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        import math

        res: List[int] = []
        while label >= 1:
            res.append(label)
            level = int(math.log(label, 2))
            label = 2 ** level - 1 + 2 ** (level - 1) - label // 2
        return res[::-1]


if __name__ == "__main__":
    print(Solution().pathInZigZagTree(label=14))
