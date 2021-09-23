# -*- coding:utf-8 -*-
# @Time     : 2021/6/24 23: 26
# @Author   : Ranshi
# @File     : 面试题 01.01. 判定字符是否唯一.py
class Solution:
    def isUnique(self, astr: str) -> bool:
        bit_flag = 0
        for ch in astr:
            x = ord(ch) - ord("a")
            if (bit_flag >> x) & 1 == 0:
                bit_flag |= 1 << x
            else:
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.isUnique("leetcode"))
