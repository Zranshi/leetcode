# -*- coding: UTF-8 -*-
# @Time     : 2022/09/12 09:46
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 剑指 Offer II 017. 含有所有字符的最短字符串

from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_chr, idx_chr = Counter(t), Counter("")
        ans = s

        def is_contain(container: Counter, obj: Counter):
            return all(key in container and container[key] >= obj[key] for key in obj.keys())

        if not is_contain(Counter(s), t_chr):
            return ""

        left = 0
        for right in range(len(s)):
            idx_chr[s[right]] += 1
            while is_contain(idx_chr, t_chr):
                if len(ans) > right - left + 1:
                    ans = s[left : right + 1]
                idx_chr[s[left]] -= 1
                left += 1
        return ans


if __name__ == "__main__":
    print(Solution().minWindow(s="ADOBECODEBANC", t="ABC"))
