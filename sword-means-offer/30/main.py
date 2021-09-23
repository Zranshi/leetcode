# -*- coding: UTF-8 -*-
# @Time     : 2021/09/23 08:27
# @Author   : Ranshi
# @File     : main.py
class MinStack:
    def __init__(self):
        self._main_stk = []
        self._min_stk = []

    def push(self, x: int) -> None:
        self._main_stk.append(x)
        if not self._min_stk or self._min_stk[-1] >= x:
            self._min_stk.append(x)

    def pop(self) -> None:
        if self._main_stk.pop() == self._min_stk[-1]:
            self._min_stk.pop()

    def top(self) -> int:
        return self._main_stk[-1]

    def min(self) -> int:
        return self._min_stk[-1]
