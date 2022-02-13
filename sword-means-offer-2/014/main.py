# -*- coding: UTF-8 -*-
# @Time     : 2022/01/09 09:14
# @Author   : Ranshi
# @File     : 123.py
# @Doc      : 剑指 Offer II 014. 字符串中的变位词
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        if len1 > len2:
            return False
        ch_count1 = [0] * 26
        ch_count2 = [0] * 26

        for ch in s1:
            ch_count1[ord(ch) - 97] += 1

        for i in range(len1):
            ch_count2[ord(s2[i]) - 97] += 1

        for left in range(0, len2 - len1):
            if all(ch_count1[i] == ch_count2[i] for i in range(26)):
                return True
            ch_count2[ord(s2[left]) - 97] -= 1
            ch_count2[ord(s2[left + len1]) - 97] += 1
        else:
            if all(ch_count1[i] == ch_count2[i] for i in range(26)):
                return True

        return False


if __name__ == "__main__":
    print(Solution().checkInclusion(s1="ab", s2="eidbaooo"))
