# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 01
# @Author   : Ranshi
# @File     : 125. 验证回文串.py
import string


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        char_list = []
        num_map = {str(i) for i in range(0, 10)}
        char_map = set(string.ascii_lowercase)
        for i in s:
            if i in num_map or i in char_map:
                char_list.append(i)
        if not char_list:
            return True
        i, j = 0, len(char_list) - 1
        while i < j:
            if char_list[i] != char_list[j]:
                return False
            i += 1
            j -= 1
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome("0P"))
