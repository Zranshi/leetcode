# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 17: 58
# @Author   : Ranshi
# @File     : 91. 解码方法.py
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        a, b, c = 0, 1, 0
        for i in range(1, n + 1):
            c = 0
            if s[i - 1] != '0':
                c += b
            if i > 1 and s[i - 2] != '0' and int(s[i - 2:i]) <= 26:
                c += a
            a, b = b, c
        return c


if __name__ == '__main__':
    s = Solution()
    print(s.numDecodings(s="111111111111111111111111111111111111111111111"))
