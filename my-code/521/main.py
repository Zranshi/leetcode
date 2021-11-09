# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 10
# @Author   : Ranshi
# @File     : 521. 最长特殊序列-ⅰ.py
class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        return max(len(a), len(b)) if a != b else -1


if __name__ == "__main__":
    s = Solution()
    print(s.findLUSlength("aba", "cdc"))
