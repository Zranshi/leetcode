# -*- coding:utf-8 -*-
# @Time     : 2021/5/19 22:28
# @Author   : Ranshi
# @File     : 470. 用 Rand7() 实现 Rand10().py
def rand7() -> int:
    pass


class Solution:
    def rand10(self) -> int:
        while True:
            res = (rand7() - 1) * 7 + rand7()
            if res <= 40:
                break
        return res % 10 + 1
