# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 09
# @Author   : Ranshi
# @File     : 387. 字符串中的第一个唯一字符.py
class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        c = Counter(s)
        for i in range(len(s)):
            if c[s[i]] == 1:
                return i
        return -1


if __name__ == "__main__":
    s = Solution()
    print(s.firstUniqChar("leetcode"))
