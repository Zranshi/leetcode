# -*- coding:utf-8 -*-
# @Time     : 2021/6/29 08: 23
# @Author   : Ranshi
# @File     : 面试题 03.03. 堆盘子.py
class StackOfPlates:

    def __init__(self, cap: int):
        self.cap = cap
        self.stacks = []

    def push(self, val: int) -> None:
        if self.cap <= 0:
            return
        elif not self.stacks or len(self.stacks[-1]) == self.cap:
            self.stacks.append([val])
        else:
            self.stacks[-1].append(val)

    def pop(self) -> int:
        if self.stacks:
            x = self.stacks[-1].pop()
        else:
            x = -1
        if self.stacks and not self.stacks[-1]:
            self.stacks.pop()
        return x

    def popAt(self, index: int) -> int:
        if index >= len(self.stacks):
            return -1
        x = self.stacks[index].pop()
        if not self.stacks[index]:
            self.stacks.pop(index)
        return x
