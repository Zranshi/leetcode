# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 09
# @Author   : Ranshi
# @File     : 448. 找到所有数组中消失的数字.py
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        c = set(nums)
        return [i for i in range(1, len(nums) + 1) if i not in c]


if __name__ == "__main__":
    s = Solution()
    print(s.findDisappearedNumbers([1, 1]))
