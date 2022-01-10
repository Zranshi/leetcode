# -*- coding: UTF-8 -*-
# @Time     : 2022/01/09 09:18
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 剑指 Offer II 016. 不含重复字符的最长子字符串
class Solution:
    def lengthOfLongestSubstring(self, s):
        calc = {}
        left = 0
        ret = 0
        for i, j in enumerate(s):
            if j in calc:
                left = max(left, calc[j] + 1)
            calc[j] = i
            ret = max(ret, i - left + 1)
        return ret


if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring(s="abcabcbb"))
