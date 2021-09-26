# -*- coding: UTF-8 -*-
# @Time     : 2021/09/25 07:45
# @Author   : Ranshi
# @File     : main.py
class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return (s + s[:n])[n:]


if __name__ == "__main__":
    print(Solution().reverseLeftWords(s="abcdefg", n=2))
