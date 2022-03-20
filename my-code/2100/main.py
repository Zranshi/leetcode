# -*- coding: UTF-8 -*-
# @Time     : 2022/03/13 14:00
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 2100. 适合打劫银行的日子
class Solution:
    def goodDaysToRobBank(self, security: list[int], time: int) -> list[int]:
        res = []
        pre, post = [0] * len(security), [0] * len(security)
        for i in range(1, len(security)):
            if security[i] <= security[i - 1]:
                pre[i] = pre[i - 1] + 1
            else:
                pre[i] = 0
        for i in range(len(security) - 2, -1, -1):
            if security[i] <= security[i + 1]:
                post[i] = post[i + 1] + 1
            else:
                post[i] = 0
        for i in range(len(security)):
            if pre[i] >= time and post[i] >= time:
                res.append(i)
        return res


print(Solution().goodDaysToRobBank(security=[5, 3, 3, 3, 5, 6, 2], time=2))
