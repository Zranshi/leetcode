# -*- coding: UTF-8 -*-
# @Time     : 2022/10/15 14:18
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 剑指 Offer II 058. 日程表
class MyCalendar:
    def __init__(self):
        self.tree = set()
        self.lazy = set()

    def query(self, start: int, end: int, left: int, right: int, idx: int) -> bool:
        if right < start or end < left:
            return False
        if idx in self.lazy:
            return True
        if start <= left and right <= end:
            return idx in self.tree
        mid = (left + right) // 2
        return self.query(start, end, left, mid, idx * 2) or self.query(
            start, end, mid + 1, right, idx * 2 + 1
        )

    def update(self, start: int, end: int, left: int, right: int, idx: int) -> None:
        if right < start or end < left:
            return
        if start <= left and right <= end:
            self.tree.add(idx)
            self.lazy.add(idx)
        else:
            mid = (left + right) // 2
            self.update(start, end, left, mid, idx * 2)
            self.update(start, end, mid + 1, right, idx * 2 + 1)
            self.tree.add(idx)
            if idx * 2 in self.lazy and idx * 2 + 1 in self.lazy:
                self.lazy.add(idx)

    def book(self, start: int, end: int) -> bool:
        if self.query(start, end - 1, 0, 10**9, 1):
            return False
        self.update(start, end - 1, 0, 10**9, 1)
        return True
