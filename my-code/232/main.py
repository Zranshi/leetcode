# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 04
# @Author   : Ranshi
# @File     : 232. 用栈实现队列.py
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.inStack = []
        self.outStack = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.inStack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.outStack:
            self.outStack = self.inStack[::-1]
            self.inStack = []
        x = self.outStack[-1]
        self.outStack.pop()
        return x

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.outStack:
            self.outStack = self.inStack[::-1]
            self.inStack = []
        return self.outStack[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if self.inStack or self.outStack:
            return False
        return True


if __name__ == '__main__':
    q = MyQueue()
    q.push(4)
    q.push(7)
    print(q.pop())
    print(q.pop())
