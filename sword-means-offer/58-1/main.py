# -*- coding: UTF-8 -*-
# @Time     : 2021/10/04 13:01
# @Author   : Ranshi
# @File     : main.py
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.strip().split()[::-1])


if __name__ == "__main__":
    print(Solution().reverseWords("the sky is blue"))
