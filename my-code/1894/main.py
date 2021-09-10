# -*- coding: UTF-8 -*-
# @Time     : 2021/09/10 07:20
# @Author   : Ranshi
# @File     : main.py
from typing import List


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        idx = 0
        k = k % sum(chalk)
        while True:
            k -= chalk[idx]
            if k < 0:
                break
            idx = (idx + 1) % len(chalk)
        return idx


if __name__ == "__main__":
    print(Solution().chalkReplacer(chalk=[5, 1, 5], k=22))
