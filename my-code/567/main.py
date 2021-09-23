# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 11
# @Author   : Ranshi
# @File     : 567. 字符串的排列.py
from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_length, s2_length = len(s1), len(s2)
        s2 = s2 + "0"
        ans = Counter(s1)
        idx = Counter(s2[:s1_length])
        if s1_length > s2_length:
            return False

        for left in range(0, s2_length - s1_length + 1):
            # print(idx)
            if idx == ans:
                return True
            idx[s2[left + s1_length]] += 1
            if idx[s2[left]] == 1:
                idx.pop(s2[left])
            else:
                idx[s2[left]] -= 1
        return False


if __name__ == "__main__":
    s = Solution()
    print(s.checkInclusion("ab", "eidboaoo"))
