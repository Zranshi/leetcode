# -*- coding: UTF-8 -*-
# @Time     : 2021/08/26 07:10
# @Author   : Ranshi
# @File     : main.py

from typing import List


class Solution:

    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        res = 0
        le, ri = 0, len(people) - 1
        while le <= ri:
            if people[le] + people[ri] <= limit:
                le, ri = le + 1, ri - 1
            else:
                ri = ri - 1
            res += 1
        return res


if __name__ == '__main__':
    print(Solution().numRescueBoats(people=[3, 2, 2, 1], limit=3))
