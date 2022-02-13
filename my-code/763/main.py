#!/usr/bin/env python3
# coding: utf-8
# @Time     : 2021/08/11 12:13
# @Author   : Ranshi
# @File     : 123.py

from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        ch_range = [[] for _ in range(26)]
        for i in range(len(s)):
            idx = ord(s[i]) - ord("a")
            if not ch_range[idx]:
                ch_range[idx] = [i, i]
            else:
                ch_range[idx][1] = i
        ranges = sorted([item for item in ch_range if item], key=lambda x: x[0])
        idx = ranges[0]
        for v in ranges:
            if v[0] > idx[1]:
                res.append(idx[1] - idx[0] + 1)
                idx = v
            elif v[1] > idx[1]:
                idx[1] = v[1]
        else:
            res.append(idx[1] - idx[0] + 1)
        return res


if __name__ == "__main__":
    print(Solution().partitionLabels("ababcbacadefegdehijhklij"))
