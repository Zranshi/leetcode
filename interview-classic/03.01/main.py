# -*- coding:utf-8 -*-
# @Time     : 2021/6/28 21: 13
# @Author   : Ranshi
# @File     : 面试题 03.01. 三合一.py
class TripleInOne:
    def __init__(self, stack_size: int):
        self.max_len = stack_size
        self.stack = [[], [], []]

    def push(self, stack_num: int, value: int) -> None:
        if len(self.stack[stack_num]) < self.max_len:
            self.stack[stack_num].append(value)

    def pop(self, stack_num: int) -> int:
        if self.stack[stack_num]:
            return self.stack[stack_num].pop()
        else:
            return -1

    def peek(self, stack_num: int) -> int:
        if self.stack[stack_num]:
            return self.stack[stack_num][-1]
        else:
            return -1

    def isEmpty(self, stack_num: int) -> bool:
        return len(self.stack[stack_num]) == 0


# Your TripleInOne object will be instantiated and called as such:
# obj = TripleInOne(stackSize)
# obj.push(stackNum,value)
# param_2 = obj.pop(stackNum)
# param_3 = obj.peek(stackNum)
# param_4 = obj.isEmpty(stackNum)
