# -*- coding:utf-8 -*-
# @Time     : 2021/07/29 00:38
# @Author   : Ranshi
# @File     : main.py


class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([item[::-1] for item in s.split(" ")])


if __name__ == "__main__":
    print(Solution().reverseWords("Let's take  LeetCode contest"))
