# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 17: 50
# @Author   : Ranshi
# @File     : 13. 罗马数字转整数.py
class Solution:
    def romanToInt(self, s):
        a = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        ans = 0
        for i in range(len(s)):
            if i < len(s) - 1 and a[s[i]] < a[s[i + 1]]:
                ans -= a[s[i]]
            else:
                ans += a[s[i]]
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.romanToInt("MCMXCIV"))
