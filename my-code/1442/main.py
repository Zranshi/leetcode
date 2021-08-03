# -*- coding:utf-8 -*-
# @Time     : 2021/05/18 08: 53
# @Author   : Ranshi
# @File     : 1442. 形成两个异或相等数组的三元组数目.py
from typing import List


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        from collections import Counter
        cnt, total = Counter(), Counter()
        ans, s = 0, 0
        for k, val in enumerate(arr):
            if (t := s ^ val) in cnt:
                ans += cnt[t] * k - total[t]
            cnt[s] += 1
            total[s] += k
            s = t
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.countTriplets(arr=[2, 3, 1, 6, 7]))
