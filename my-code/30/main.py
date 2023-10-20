# -*- coding: UTF-8 -*-
# @Time     : 2023/10/19 17:01
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 30. 串联所有单词的子串
from collections import Counter


class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        word_width = len(words[0])
        length = len(words) * word_width
        res = []
        words_counter = Counter(words)

        if len(s) < length:
            return res

        left = 0
        while left <= len(s) - length:
            flag = True
            counter = words_counter.copy()

            for i in range(left, left + length, word_width):
                meta_string = s[i : i + word_width]
                if meta_string not in counter:
                    flag = False
                    break
                counter[meta_string] -= 1

            if flag and all([item == 0 for item in counter.values()]):
                res.append(left)

            left += 1

        return res


print(
    Solution().findSubstring(
        s="wordgoodgoodgoodbestword", words=["word", "good", "best", "good"]
    )
)
