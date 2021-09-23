# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 15
# @Author   : Ranshi
# @File     : 844. 比较含退格的字符串.py
class Solution:
    def backspaceCompare1(self, S: str, T: str) -> bool:
        i, j = len(S) - 1, len(T) - 1
        skipS = skipT = 0
        while i >= 0 or j >= 0:
            while i >= 0:
                if S[i] == "#":
                    skipS += 1
                    i -= 1
                elif skipS > 0:
                    skipS -= 1
                    i -= 1
                else:
                    break
            while j >= 0:
                if T[j] == "#":
                    skipT += 1
                    j -= 1
                elif skipT > 0:
                    skipT -= 1
                    j -= 1
                else:
                    break
            if i >= 0 and j >= 0:
                if S[i] != T[j]:
                    return False
            elif i >= 0 or j >= 0:
                return False
            i -= 1
            j -= 1
        return True

    def backspaceCompare(self, S: str, T: str) -> bool:
        import re

        def f(s):
            while "#" in s:
                s = re.sub("(?:^|[^#])#", "", s)
            return s

        return f(S) == f(T)


if __name__ == "__main__":
    s = Solution()
    print(s.backspaceCompare(S="ab#c", T="ad#c"))
