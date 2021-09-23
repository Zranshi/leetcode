# -*- coding:utf-8 -*-
# @Time     : 2021/5/20 08:30
# @Author   : Ranshi
# @File     : 692. 前K个高频单词.py
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        from collections import Counter

        word_freq = Counter(words)
        return sorted(list(word_freq), lambda x: (-1 * word_freq[x], x))[:k]


if __name__ == "__main__":
    s = Solution()
    print(
        s.topKFrequent(
            [
                "the",
                "day",
                "is",
                "sunny",
                "the",
                "the",
                "the",
                "sunny",
                "is",
                "is",
            ],
            k=4,
        )
    )
