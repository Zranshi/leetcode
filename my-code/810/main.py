# -*- coding:utf-8 -*-
# @Time     : 2021/5/25 07:27
# @Author   : Ranshi
# @File     : 810. 黑板异或游戏.py
from functools import reduce
from operator import xor
from typing import List


class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        if len(nums) % 2 == 0:
            return True
        xor_sum = reduce(xor, nums)
        return xor_sum == 0


if __name__ == '__main__':
    s = Solution()
    print(s.xorGame(nums=[1, 1, 2]))
