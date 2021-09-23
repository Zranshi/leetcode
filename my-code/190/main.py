# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 02
# @Author   : Ranshi
# @File     : 190. 颠倒二进制位.py
class Solution:
    def reverseBits(self, n: int) -> int:
        ans, mask = 0, 1
        for i in range(32):
            if n & mask:
                ans |= 1 << (31 - i)
            mask <<= 1
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.reverseBits(964176192))
