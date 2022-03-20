# -*- coding: UTF-8 -*-
# @Time     : 2022/02/23 19:14
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 917. 仅仅反转字母
import string

AVALIABLE_CHS = {ch for ch in string.ascii_letters}


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and s[left] not in AVALIABLE_CHS:
                left += 1
            while left < right and s[right] not in AVALIABLE_CHS:
                right -= 1
            if left < right:
                s[left], s[right] = s[right], s[left]
                left, right = left + 1, right - 1
        return "".join(s)


if __name__ == "__main__":
    print(Solution().reverseOnlyLetters(s="ab-cd"))
