# -*- coding: UTF-8 -*-
# @Time     : 2021/08/19 07:19
# @Author   : Ranshi
# @File     : 123.py


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = {"a", "o", "e", "i", "u", "A", "O", "E", "I", "U"}
        chs = list(s)
        lo, hi = 0, len(chs) - 1
        while lo < hi:
            while chs[lo] not in vowel and lo < hi:
                lo += 1
            while chs[hi] not in vowel and lo < hi:
                hi -= 1
            chs[lo], chs[hi] = chs[hi], chs[lo]
            lo, hi = lo + 1, hi - 1
        return "".join(chs)


if __name__ == "__main__":
    print(Solution().reverseVowels("ai"))
