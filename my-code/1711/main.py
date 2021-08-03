# -*- coding:utf-8 -*-
# @Time     : 2021/7/7 09: 43
# @Author   : Ranshi
# @File     : main.py
from typing import List


class Solution:
    powersOfTwo = [2 ** i for i in range(22)]
    mod = 10 ** 9 + 7

    def countPairs(self, deliciousness: List[int]) -> int:
        from collections import Counter
        cnts, ans = Counter(), 0
        for num in deliciousness:
            for target in self.powersOfTwo:
                ans += cnts[target - num]
            cnts[num] += 1
        return ans % self.mod


if __name__ == '__main__':
    s = Solution()
    print(s.countPairs(deliciousness=[149, 107, 1, 63, 0, 1, 6867, 1325, 5611, 2581, 39, 89, 46, 18, 12, 20, 22, 234]))
