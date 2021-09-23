# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 15
# @Author   : Ranshi
# @File     : 842. 将数组拆分成斐波那契序列.py
from typing import List


class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        INT_MAX = 2 ** 31 - 1
        ans = []

        def backtrack(index: int):
            if index == len(S):
                return len(ans) >= 3
            curr = 0
            for i in range(index, len(S)):
                if i > index and S[index] == "0":
                    break
                curr = curr * 10 + ord(S[i]) - ord("0")
                if curr > INT_MAX:
                    break
                if len(ans) < 2 or curr == ans[-2] + ans[-1]:
                    ans.append(curr)
                    if backtrack(i + 1):
                        return True
                    ans.pop()
                elif len(ans) > 2 and curr > ans[-2] + ans[-1]:
                    break
            return False

        backtrack(0)
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.splitIntoFibonacci("11235813"))
