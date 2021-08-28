# -*- coding: UTF-8 -*-
# @Time     : 2021/08/28 08:58
# @Author   : Ranshi
# @File     : main.py

from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = nums[:]
        for i in range(1, len(res)):
            res[i] += res[i - 1]
        return res


if __name__ == '__main__':
    print(Solution().runningSum(nums=[1]))
