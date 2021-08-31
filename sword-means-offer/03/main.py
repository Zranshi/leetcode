# -*- coding:utf-8 -*-
# @Time     : 2021/8/2 18:47
# @Author   : Ranshi
# @File     : main.py
from typing import List


class Solution:

    def findRepeatNumber(self, nums: List[int]) -> int:
        s = set()
        for x in nums:
            if x in s:
                return x
            else:
                s.add(x)
        return -1


if __name__ == '__main__':
    print(Solution().findRepeatNumber([2, 3, 1, 0, 2, 5, 3]))
