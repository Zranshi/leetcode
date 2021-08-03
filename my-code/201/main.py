# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 02
# @Author   : Ranshi
# @File     : 201. 数字范围按位与.py
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        while m < n:
            # 抹去最右边的 1
            n = n & (n - 1)
        return n


if __name__ == "__main__":
    s = Solution()
    print(s.rangeBitwiseAnd(5, 7))
