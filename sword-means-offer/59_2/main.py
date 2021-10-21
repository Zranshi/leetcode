#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/10/21 09:52
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 剑指 Offer 59 - II. 队列的最大值
import queue


class MaxQueue:
    def __init__(self):
        self.deque = queue.deque()
        self.queue = queue.Queue()

    def max_value(self) -> int:
        return self.deque[0] if self.deque else -1

    def push_back(self, value: int) -> None:
        while self.deque and self.deque[-1] < value:
            self.deque.pop()
        self.deque.append(value)
        self.queue.put(value)

    def pop_front(self) -> int:
        if not self.deque:
            return -1
        ans = self.queue.get()
        if ans == self.deque[0]:
            self.deque.popleft()
        return ans
