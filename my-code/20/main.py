# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 17: 50
# @Author   : Ranshi
# @File     : 20. 有效的括号.py
class Solution:
    def isValid(self, string: str) -> bool:
        stack, front, back = [], ['(', '[', '{'], [')', ']', '}']
        for x in string:
            if x in front:
                stack.append(x)
            else:
                if stack and front.index(stack[-1]) == back.index(x):
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isValid(string="()]{}"))
