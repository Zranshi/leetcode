# -*- coding:utf-8 -*-
# @Time     : 2021/6/25 13: 33
# @Author   : Ranshi
# @File     : 面试题 01.05. 一次编辑.py
class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        if abs(len(first) - len(second)) > 1:
            return False
        if len(first) > len(second):
            first, second = second, first
        for i in range(len(first)):
            if first[i] == second[i]:
                continue
            return (
                first[i:] == second[i + 1 :]
                or first[i + 1 :] == second[i + 1 :]
            )
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.oneEditAway(first="pale", second="ple"))
