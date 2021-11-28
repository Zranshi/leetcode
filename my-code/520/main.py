#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/11/13 09:47
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 520. 检测大写字母
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # 若第 1 个字母为小写，则需额外判断第 2 个字母是否为小写
        if len(word) >= 2 and word[0].islower() and word[1].isupper():
            return False

        # 无论第 1 个字母是否大写，其他字母必须与第 2 个字母的大小写相同
        return all(word[i].islower() == word[1].islower() for i in range(2, len(word)))


if __name__ == "__main__":
    print(Solution().detectCapitalUse(word="USA"))
