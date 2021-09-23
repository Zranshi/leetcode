# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 09
# @Author   : Ranshi
# @File     : 424. 替换后的最长重复字符.py
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right, length, max_len = 0, 0, len(s), 0
        chars = [0 for _ in range(26)]
        while right < length:
            chars[ord(s[right]) - ord("A")] += 1
            max_len = max(max_len, chars[ord(s[right]) - ord("A")])
            if right - left + 1 - max_len > k:
                chars[ord(s[left]) - ord("A")] -= 1
                left += 1
            right += 1
        return right - left


if __name__ == "__main__":
    s = Solution()
    print(s.characterReplacement(s="AABABBA", k=1))
