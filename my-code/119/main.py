# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 00
# @Author   : Ranshi
# @File     : 119. 杨辉三角 II.py
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1, 1]
        if rowIndex == 0:
            return [1]
        for i in range(2, rowIndex + 1):
            res = (
                [1]
                + [res[j] + res[j + 1] for j in range(0, len(res) - 1)]
                + [1]
            )
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.getRow(4))
