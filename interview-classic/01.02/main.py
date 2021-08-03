# -*- coding:utf-8 -*-
# @Time     : 2021/6/24 23: 41
# @Author   : Ranshi
# @File     : 面试题 01.02. 判定是否互为字符重排.py
class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        arr = [0] * 26
        for ch in s1:
            arr[ord(ch) - ord('a')] += 1
        for ch in s2:
            arr[ord(ch) - ord('a')] -= 1
        for x in arr:
            if x != 0:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.CheckPermutation(s1="abc", s2="bad"))
