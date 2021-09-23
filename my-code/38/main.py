# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 17: 51
# @Author   : Ranshi
# @File     : 38. 外观数列.py


class Solution:
    def countAndSay(self, n: int) -> str:
        countStr = "1"
        for _ in range(1, n):
            left, right, nextStr = 0, 0, ""
            for right in range(len(countStr)):
                if countStr[right] != countStr[left]:
                    nextStr += str(right - left) + countStr[left]
                    left = right
            nextStr += str(right - left + 1) + countStr[left]
            countStr = nextStr
        return countStr


if __name__ == "__main__":
    s = Solution()
    print(s.countAndSay(4))
