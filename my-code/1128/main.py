# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 18
# @Author   : Ranshi
# @File     : 1128. 等价多米诺骨牌对的数量.py
from typing import List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        num = [0] * 100
        ret = 0
        for x, y in dominoes:
            val = (x * 10 + y if x <= y else y * 10 + x)
            ret += num[val]
            num[val] += 1
        return ret


if __name__ == '__main__':
    s = Solution()
    print(s.numEquivDominoPairs(dominoes=[[1, 2], [2, 1], [3, 4], [5, 6]]))
