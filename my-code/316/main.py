# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 07
# @Author   : Ranshi
# @File     : 316. 去除重复字母.py
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        """
        栈
        """
        from collections import Counter

        c = Counter(s)
        stack = []
        existed = set()
        for a in s:
            if a not in existed:
                while stack and stack[-1] > a and c[stack[-1]] > 0:
                    existed.remove(stack.pop())
                stack.append(a)
                existed.add(a)
            c[a] -= 1
        return "".join(stack)


if __name__ == "__main__":
    s = Solution()
    print(s.removeDuplicateLetters(s="bcabc"))
