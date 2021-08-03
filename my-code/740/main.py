# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 13
# @Author   : Ranshi
# @File     : 740. 删除并获得点数.py
from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        val = max(nums)
        total = [0] * (val + 1)
        for item in nums:
            total[item] += item

        size = len(total)
        first, second = total[0], max(total[0], total[1])
        for i in range(2, size):
            first, second = second, max(first + total[i], second)
        return second


if __name__ == '__main__':
    s = Solution()
    print(s.deleteAndEarn(nums=[2, 2, 3, 3, 3, 4]))
