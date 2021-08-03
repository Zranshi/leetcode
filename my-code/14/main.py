# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 17: 50
# @Author   : Ranshi
# @File     : 14. 最长公共前缀.py
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        length = len(strs)
        if length == 1:
            return strs[0]
        strs.sort()
        for i in range(len(strs[0])):
            if strs[0][i] != strs[-1][i]:
                return strs[0][:i]
        return strs[0]


if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix(strs=["dog", "racecar", "car"]))
