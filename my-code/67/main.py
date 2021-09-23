# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 17: 52
# @Author   : Ranshi
# @File     : 67. 二进制求和.py
class Solution:
    def addBinary(self, a, b) -> str:
        return "{0:b}".format(int(a, 2) + int(b, 2))


if __name__ == "__main__":
    s = Solution()
    print(s.addBinary(a="1", b="11"))
