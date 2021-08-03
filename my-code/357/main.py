# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 07
# @Author   : Ranshi
# @File     : 357. 计算各个位数不同的数字个数.py
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        from functools import reduce
        res = 0
        if n == 1:
            return 10
        elif n == 0:
            return 1
        for idx in range(1, n + 1):
            if idx != 1:
                res += reduce(lambda x, y: x * y,
                              [item for item in range(
                                  9, 9 - idx + 1, -1)] + [9])
            else:
                res += 10
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.countNumbersWithUniqueDigits(3))
