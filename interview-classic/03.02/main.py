# -*- coding:utf-8 -*-
# @Time     : 2021/6/29 08: 05
# @Author   : Ranshi
# @File     : 面试题 03.02. 栈的最小值.py


class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.min_stack or self.min_stack[-1] > x:
            self.min_stack.append(x)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


if __name__ == '__main__':
    ms = MinStack()
    ms.push(0)
    ms.push(1)
    ms.push(0)
    x = ms.getMin()
    ms.pop()
    y = ms.getMin()
