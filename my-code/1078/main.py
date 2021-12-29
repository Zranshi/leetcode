# -*- coding: UTF-8 -*-
# @Time     : 2021/12/26 18:37
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 1078. Bigram 分词
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> list[str]:
        words = text.split()
        return [
            words[i]
            for i in range(2, len(words))
            if words[i - 2] == first and words[i - 1] == second
        ]


if __name__ == "__main__":
    print(
        Solution().findOcurrences(
            text="alice is a good girl she is a good student", first="a", second="good"
        )
    )
