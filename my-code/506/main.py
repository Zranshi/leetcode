#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/12/02 09:09
# @Author   : Ranshi
# @File     : 123.py
# @Doc      : 506. 相对名次
class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        rank = sorted(score, reverse=True)
        ranking = {v: i + 1 for i, v in enumerate(rank)}
        res = []
        for item in score:
            if ranking[item] == 1:
                res.append("Gold Medal")
            elif ranking[item] == 2:
                res.append("Silver Medal")
            elif ranking[item] == 3:
                res.append("Bronze Medal")
            else:
                res.append(str(ranking[item]))
        return res


if __name__ == "__main__":
    print(Solution().findRelativeRanks(score=[5, 4, 3, 2, 1]))
