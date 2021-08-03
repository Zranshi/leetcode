# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 09
# @Author   : Ranshi
# @File     : 395. 至少有K个重复字符的最长子串.py
class Solution(object):
    def longestSubstring(self, s, k):
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)


# class Solution(object):
#     def longestSubstring(self, s, k):
#         for t in range(1, 27):
#             left, total, cnt, less = 0, 0, [0 for _ in range(26)], 0
#             for right in range(len(s)):
#                 idx = ord(s[right]) - ord('a')
#                 cnt[idx] += 1
#                 if cnt[idx] == 1:
#                     total += 1
#                 if cnt[idx] > k:
#                     less += 1


if __name__ == '__main__':
    s = Solution()
    print(s.longestSubstring(s="aaabb", k=3))
