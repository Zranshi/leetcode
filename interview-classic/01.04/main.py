# -*- coding:utf-8 -*-
# @Time     : 2021/6/25 12: 42
# @Author   : Ranshi
# @File     : 面试题 01.04. 回文排列.py
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        from collections import Counter
        c = Counter(s)
        oi = 0
        for key in c:
            if c[key] % 2 == 1:
                if oi == 1:
                    return False
                oi += 1
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.canPermutePalindrome("tactcoa"))
