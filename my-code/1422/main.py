# -*- coding: UTF-8 -*-
# @Time     : 2022/08/14 17:03
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 1422. 分割字符串的最大得分
class Solution:
    def maxScore(self, s: str) -> int:
        score = (1 if s[0] == "0" else 0) + len([item for item in s[1:] if item == "1"])
        res = score
        for ch in s[1:-1]:
            score += 1 if ch == "0" else -1
            res = max(score, res)
        return res


if __name__ == "__main__":
    print(Solution().maxScore(s="00"))
