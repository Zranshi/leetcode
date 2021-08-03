# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 14
# @Author   : Ranshi
# @File     : 765. 情侣牵手.py
from typing import List


class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        def find_another(n) -> int:
            if n % 2 == 0:
                return n + 1
            else:
                return n - 1

        c = 0
        for i in range(0, len(row), 2):
            p1 = row[i]
            p2 = find_another(p1)
            if row[i + 1] != p2:
                j = row.index(p2)
                row[i + 1], row[j] = row[j], row[i + 1]
                c += 1
        return c


if __name__ == '__main__':
    s = Solution()
    print(s.minSwapsCouples(row=[0, 2, 1, 3]))
