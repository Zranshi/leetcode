# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 20
# @Author   : Ranshi
# @File     : 1423. 可获得的最大点数.py
from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        res, idx = sum(cardPoints[:k]), 0
        ans = res
        while idx < k:
            ans = ans - cardPoints[k - idx - 1] + cardPoints[-(idx + 1)]
            res = max(res, ans)
            idx += 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.maxScore(cardPoints=[1, 2, 3, 4, 5, 6, 1], k=3))
