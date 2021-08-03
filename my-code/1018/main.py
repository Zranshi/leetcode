# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 18
# @Author   : Ranshi
# @File     : 1018. 可被 5 整除的二进制前缀.py
from typing import List


class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        res = []
        idx = 0
        for x in A:
            idx = idx % 5
            idx = idx << 1
            idx += x
            if idx % 5 == 0:
                res.append(True)
            else:
                res.append(False)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.prefixesDivBy5([0, 1, 1]))
