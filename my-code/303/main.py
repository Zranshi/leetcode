# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 07
# @Author   : Ranshi
# @File     : 303. 区域和检索 - 数组不可变.py
from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        self.sums = [0]

        for num in nums:
            self.sums.append(self.sums[-1] + num)

    def sumRange(self, i: int, j: int) -> int:
        return self.sums[j + 1] - self.sums[i]


if __name__ == "__main__":
    numArray = NumArray([-2, 0, 3, -5, 2, -1])
    print(numArray.sumRange(0, 2))
    print(numArray.sumRange(2, 5))
