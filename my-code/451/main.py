# -*- coding:utf-8 -*-
# @Time     : 2021/7/3 08: 25
# @Author   : Ranshi
# @File     : main.py
class Solution:
    def frequencySort(self, string: str) -> str:
        from collections import Counter
        chd = Counter(string)
        chl = [(ch, chd[ch]) for ch in chd]
        chl.sort(key=lambda x: x[1], reverse=True)
        return ''.join([item[0] * item[1] for item in chl])


if __name__ == '__main__':
    s = Solution()
    print(s.frequencySort("tree"))
