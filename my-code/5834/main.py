# -*- coding: UTF-8 -*-
# @Time     : 2021/08/21 22:30
# @Author   : Ranshi
# @File     : 123.py


class Solution:
    def minTimeToType(self, word: str) -> int:
        res = 0
        idx_ch = "a"
        for ch in word:
            path = abs(ord(idx_ch) - ord(ch))
            res += (path if path < 26 - path else 26 - path) + 1
            idx_ch = ch
        return res


if __name__ == "__main__":
    print(Solution().minTimeToType("zjpc"))
