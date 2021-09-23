# -*- coding: utf-8 - *-
# @Time     : 2021/05/28 17: 49
# @Author   : Ranshi
# @File     : 9. 回文数.py


class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        re_x = str_x[::-1]
        if str_x == re_x:
            return True
        return False


if __name__ == "__main__":
    print(Solution().isPalindrome(123321))
