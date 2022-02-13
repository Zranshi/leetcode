#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/10/31 08:45
# @Author   : Ranshi
# @File     : 123.py
# @Doc      : 500. 键盘行
class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        lines = [{ch for ch in line} for line in ["qwertyuiop", "asdfghjkl", "zxcvbnm"]]
        res = []
        for word in words:
            flag = -1
            jump_flag = False
            for ch in word:
                ch = ch.lower()
                for i in range(3):
                    if ch in lines[i]:
                        if flag != i:
                            if flag == -1:
                                flag = i
                            else:
                                jump_flag = True
                if jump_flag:
                    break
            if not jump_flag:
                res.append(word)
        return res


if __name__ == "__main__":
    print(Solution().findWords(words=["Hello", "Alaska", "Dad", "Peace"]))
