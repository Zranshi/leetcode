# -*- coding:utf-8 -*-
# @Time     : 2021/6/22 07: 57
# @Author   : Ranshi
# @File     : 1239. 串联字符串的最大长度.py
from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        masks = list()
        for s in arr:
            mask = 0
            for ch in s:
                idx = ord(ch) - ord('a')
                if (mask >> idx) & 1:
                    mask = 0
                    break
                mask |= 1 << idx
            if mask > 0:
                masks.append(mask)
        ans = 0

        def backtrack(pos: int, mask: int) -> None:
            if pos == len(masks):
                nonlocal ans
                ans = max(ans, bin(mask).count("1"))
                return
            if (mask & masks[pos]) == 0:
                backtrack(pos + 1, mask | masks[pos])
            backtrack(pos + 1, mask)

        backtrack(0, 0)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.maxLength(arr=["un", "iq", "ue"]))
