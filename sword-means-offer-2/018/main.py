# -*- coding: UTF-8 -*-
# @Time     : 2022/09/12 16:35
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 剑指 Offer II 018. 有效的回文
import string


class Solution:
    def isPalindrome(self, s: str) -> bool:
        ch_area = string.ascii_letters + string.digits
        chs = "".join(ch for ch in s if ch in ch_area).lower()
        return chs == chs[::-1]


if __name__ == "__main__":
    print(Solution().isPalindrome(s="A man, a plan, a canal: Panama"))
