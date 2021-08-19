# -*- coding: UTF-8 -*-
# @Time     : 2021/08/18 12:42
# @Author   : Ranshi
# @File     : main.py
class Solution:

    def minRemoveToMakeValid(self, s: str) -> str:
        indexes_to_remove = set()
        stack = []
        for i, c in enumerate(s):
            if c not in "()":
                continue
            if c == "(":
                stack.append(i)
            elif not stack:
                indexes_to_remove.add(i)
            else:
                stack.pop()
        indexes_to_remove = indexes_to_remove.union(set(stack))
        string_builder = []
        for i, c in enumerate(s):
            if i not in indexes_to_remove:
                string_builder.append(c)
        return "".join(string_builder)


if __name__ == '__main__':
    print(Solution().minRemoveToMakeValid(s="lee(t(c)o)de)"))
