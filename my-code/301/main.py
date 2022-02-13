#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/10/27 08:11
# @Author   : Ranshi
# @File     : 123.py
# @Doc      : 301. 删除无效的括号
class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def isValid(s):
            count = 0
            for c in s:
                if c == "(":
                    count += 1
                elif c == ")":
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        ans = []
        currSet = set([s])

        while True:
            for ss in currSet:
                if isValid(ss):
                    ans.append(ss)
            if len(ans) > 0:
                return ans
            nextSet = set()
            for ss in currSet:
                for i in range(len(ss)):
                    if i > 0 and ss[i] == s[i - 1]:
                        continue
                    if ss[i] == "(" or ss[i] == ")":
                        nextSet.add(ss[:i] + ss[i + 1 :])
            currSet = nextSet


if __name__ == "__main__":
    print(Solution().removeInvalidParentheses(s="()())()"))
