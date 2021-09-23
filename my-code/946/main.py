# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 17
# @Author   : Ranshi
# @File     : 946. 验证栈序列.py
class Solution(object):
    def validateStackSequences(self, pushed, popped):
        j = 0
        stack = []
        for x in pushed:
            stack.append(x)
            while stack and j < len(popped) and stack[-1] == popped[j]:
                stack.pop()
                j += 1

        return j == len(popped)


if __name__ == "__main__":
    s = Solution()
    print(
        s.validateStackSequences(pushed=[1, 2, 3, 4, 5], popped=[4, 5, 3, 2, 1])
    )
