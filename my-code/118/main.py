# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 00
# @Author   : Ranshi
# @File     : 118. 杨辉三角.py
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        pre = []
        for i in range(numRows):
            index = [1] * (i + 1)
            if i >= 2:
                for n in range(1, i):
                    index[n] = pre[n - 1] + pre[n]
            res += [index]
            pre = index
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.generate(5))
