#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/11/23 08:14
# @Author   : Ranshi
# @File     : 123.py
# @Doc      : 859. 亲密字符串
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal:
            if len(set(s)) < len(goal):
                return True
            else:
                return False
        diff = [(a, b) for a, b in zip(s, goal) if a != b]
        return len(diff) == 2 and diff[0][0] == diff[1][1] and diff[0][1] == diff[1][0]


if __name__ == "__main__":
    print(Solution().buddyStrings(s="ab", goal="ba"))
