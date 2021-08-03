# -*- coding: utf-8 - *-
# @Time     : 2021/05/28 17: 49
# @Author   : Ranshi
# @File     : 9. 回文数.py

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        re_x = x[::-1]
        if x == re_x:
            return True
        return False
