# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 17
# @Author   : Ranshi
# @File     : 989. 数组形式的整数加法.py
from typing import List


class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        res, length = [], len(A)
        i = 1
        while K != 0 or i <= length:
            if i <= length:
                K += A[-1 * i]
                i += 1
            res.append(K % 10)
            K = K // 10
        return res[::-1]


if __name__ == "__main__":
    s = Solution()
    print(s.addToArrayForm(A=[1, 2, 0, 0], K=34))
