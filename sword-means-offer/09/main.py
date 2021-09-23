# -*- coding: UTF-8 -*-
# @Time     : 2021/09/23 08:14
# @Author   : Ranshi
# @File     : main.py


class CQueue:
    def __init__(self):
        self._push_stk = []
        self._pop_stk = []

    def appendTail(self, value: int) -> None:
        self._push_stk.append(value)

    def deleteHead(self) -> int:
        if not self._pop_stk:
            self._pop_stk = self._push_stk[::-1]
            self._push_stk = []
        return self._pop_stk.pop() if self._pop_stk else -1


if __name__ == "__main__":
    cq = CQueue()
    cq.appendTail(234)
    cq.appendTail(561)
    cq.appendTail(78)
    print(cq.deleteHead())
