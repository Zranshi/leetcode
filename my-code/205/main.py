# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 02
# @Author   : Ranshi
# @File     : 205. 同构字符串.py
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        l1, l2 = len(s), len(t)
        if l1 != l2:
            return False
        d1 = dict()
        d2 = dict()
        for i in range(l1):
            if s[i] not in d1:
                d1[s[i]] = t[i]
            elif d1[s[i]] != t[i]:
                return False
            if t[i] not in d2:
                d2[t[i]] = s[i]
            elif d2[t[i]] != s[i]:
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.isIsomorphic(s="ab", t="aa"))
