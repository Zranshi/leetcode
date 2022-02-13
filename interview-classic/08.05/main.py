# -*- coding:utf-8 -*-
# @Time     : 2021/7/20 09: 51
# @Author   : Ranshi
# @File     : 123.py
class Solution:
    def multiply(self, a: int, b: int) -> int:
        if b == 1:
            return a
        if b % 2 == 0:
            return self.multiply(a << 1, b >> 1)
        return a + self.multiply(a << 1, (b - 1) >> 1)


if __name__ == "__main__":
    s = Solution()
    print(s.multiply(1, 10))
