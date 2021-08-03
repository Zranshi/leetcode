# -*- coding:utf-8 -*-
# @Time     : 2021/5/19 15:33
# @Author   : Ranshi
# @File     : 136. 只出现一次的数字.py
from functools import reduce
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)


if __name__ == '__main__':
    s = Solution()
    print(s.singleNumber([2, 2, 1]))
