# -*- coding: UTF-8 -*-
# @Time     : 2022/01/09 09:16
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 剑指 Offer II 015. 字符串中的所有变位词
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        res = []
        len1, len2 = len(p), len(s)
        if len1 > len2:
            return []
        ch_count1 = [0] * 26
        ch_count2 = [0] * 26

        for ch in p:
            ch_count1[ord(ch) - 97] += 1

        for i in range(len1):
            ch_count2[ord(s[i]) - 97] += 1

        if all(ch_count1[i] == ch_count2[i] for i in range(26)):
            res.append(0)

        for left in range(0, len2 - len1):
            ch_count2[ord(s[left]) - 97] -= 1
            ch_count2[ord(s[left + len1]) - 97] += 1
            if all(ch_count1[i] == ch_count2[i] for i in range(26)):
                res.append(left + 1)

        return res


if __name__ == "__main__":
    print(Solution().findAnagrams(s="cbaebabacd", p="abc"))
