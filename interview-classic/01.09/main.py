# -*- coding:utf-8 -*-
# @Time     : 2021/6/27 22: 13
# @Author   : Ranshi
# @File     : 面试题 01.09. 字符串轮转.py
class Solution:

    def isFlipedString(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        return s1 in s2 + s2


if __name__ == '__main__':
    s = Solution()
    print(s.isFlipedString(s1="aa", s2="aba"))
