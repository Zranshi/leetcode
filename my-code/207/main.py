# -*- coding:utf-8 -*-
# @Time     : 2021/7/3 23: 41
# @Author   : Ranshi
# @File     : main.py
from typing import List


class Solution:
    def canFinish(
        self, num_courses: int, prerequisites: List[List[int]]
    ) -> bool:
        """
        bfs
        :param num_courses:
        :param prerequisites:
        :return:
        """
        from collections import deque

        de = deque()
        solve = []
        rely = [0 for _ in range(num_courses)]
        depends = {i: [] for i in range(num_courses)}
        for item in prerequisites:
            rely[item[0]] += 1
            depends[item[1]].append(item[0])
        for i in range(num_courses):
            if rely[i] == 0:
                de.appendleft(i)
        while de:
            idx = de.pop()
            solve.append(idx)
            if depends[idx]:
                for depend in depends[idx]:
                    rely[depend] -= 1
                    if rely[depend] == 0:
                        de.appendleft(depend)
        return len(solve) == num_courses


if __name__ == "__main__":
    s = Solution()
    print(s.canFinish(num_courses=2, prerequisites=[[1, 0]]))
