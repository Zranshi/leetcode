# -*- coding: UTF-8 -*-
# @Time     : 2021/08/31 08:24
# @Author   : Ranshi
# @File     : main.py


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        无重复字符的最长子串.

        使用滑动窗口实现, 窗口的left和right表示子串的边界,
        每次搜索是否有重复字符(使用集合判断是否重复), 在整个过程中记录最长的子串长度.

        由于只需要将right和left从头移至尾端, 故时间复杂度为O(n).

        Args:
            s (str): 目标字符串

        Returns:
            int: 最长子串的长度
        """
        mapping = set()
        left, res = 0, 0
        for right in range(len(s)):
            if s[right] in mapping:
                while s[left] != s[right]:
                    mapping.remove(s[left])
                    left += 1
                left += 1
            else:
                mapping.add(s[right])
            res = max(res, right - left + 1)
        return res


if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring(s="abcabcbb"))
