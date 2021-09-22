# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 17: 52
# @Author   : Ranshi
# @File     : 58. 最后一个单词长度.py
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(" ")[-1])


if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLastWord("Hello world"))
