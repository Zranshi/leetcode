# coding: utf-8
# @Time     : 2021/08/13 10:15
# @Author   : Ranshi
# @File     : main.py

from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        L, n = 10, len(s)
        if n <= L:
            return []
        a, aL = 4, pow(4, L)
        to_int = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        nums = [to_int.get(s[i]) for i in range(n)]

        h = 0
        seen, output = set(), set()
        for start in range(n - L + 1):
            if start != 0:
                h = h * a - nums[start - 1] * aL + nums[start + L - 1]
            else:
                for i in range(L):
                    h = h * a + nums[i]
            if h in seen:
                output.add(s[start:start + L])
            seen.add(h)
        return list(output)


if __name__ == '__main__':
    print(Solution().findRepeatedDnaSequences(s="AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
