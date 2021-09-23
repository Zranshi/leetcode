# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 17: 52
# @Author   : Ranshi
# @File     : 66. 加一.py
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(1, len(digits) + 1):
            if digits[-i] == 9:
                digits[-i] = 0
            else:
                digits[-i] += 1
                break
        if digits[0] == 0:
            return [1] + digits
        return digits


if __name__ == "__main__":
    s = Solution()
    print(s.plusOne(digits=[8, 9, 9, 9]))
