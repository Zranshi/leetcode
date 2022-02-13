#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/12/11 09:21
# @Author   : Ranshi
# @File     : 123.py
# @Doc      : 911. 在线选举
from collections import defaultdict


class TopVotedCandidate:
    def __init__(self, persons: list[int], times: list[int]):
        tops = []
        voteCounts = defaultdict()
        voteCounts[-1] = -1
        top = -1
        for p in persons:
            voteCounts[p] = voteCounts.get(p, 0) + 1
            if voteCounts[p] >= voteCounts[top]:
                top = p
            tops.append(top)
        self.tops = tops
        self.times = times

    def q(self, t: int) -> int:
        left, right = 0, len(self.times) - 1
        while left < right:
            m = left + (right - left + 1) // 2
            if self.times[m] <= t:
                left = m
            else:
                right = m - 1
        return self.tops[left]
