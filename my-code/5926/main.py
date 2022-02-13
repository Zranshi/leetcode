#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/11/14 10:30
# @Author   : Ranshi
# @File     : 123.py
# @Doc      : 5926. 买票需要的时间
from collections import deque


class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        res = 0
        for i, ticket in enumerate(tickets):
            if i < k:
                res += min(ticket, tickets[k])
            elif i > k:
                res += min(ticket, tickets[k] - 1)
        return res + tickets[k]


if __name__ == "__main__":
    print(Solution().timeRequiredToBuy(tickets=[5, 1, 1, 1], k=0))
