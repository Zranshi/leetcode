# -*- coding: UTF-8 -*-
# @Time     : 2021/10/01 08:50
# @Author   : Ranshi
# @File     : 123.py
from typing import Set


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, res = 0, 0
        chs: Set[str] = set()
        for right in range(len(s)):
            while s[right] in chs:
                chs.discard(s[left])
                left += 1
            chs.add(s[right])
            res = max(res, right - left + 1)
        return res


if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("pwwkew"))
