# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 19
# @Author   : Ranshi
# @File     : 1208. 尽可能使字符串相等.py
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        length = len(s)
        difference = [abs(ord(s[i]) - ord(t[i])) for i in range(length)]
        left = right = cost = maxLength = 0
        while right < length:
            cost += difference[right]
            while cost > maxCost:
                cost -= difference[left]
                left += 1
            maxLength = max(maxLength, right - left + 1)
            right += 1
        return maxLength


if __name__ == "__main__":
    s = Solution()
    print(
        s.equalSubstring(s="krpgjbjjznpzdfy", t="nxargkbydxmsgby", maxCost=14)
    )
