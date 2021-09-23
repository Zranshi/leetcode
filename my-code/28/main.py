# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 17: 51
# @Author   : Ranshi
# @File     : 28. 实现 strStr().py
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        length, lo = len(haystack), len(needle)
        for i in range(0, length - lo + 1):
            if needle == haystack[i : i + lo]:
                return i
        return -1


if __name__ == "__main__":
    s = Solution()
    print(s.strStr(haystack="hello", needle="ll"))
