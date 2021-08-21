# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 10
# @Author   : Ranshi
# @File     : 547. 省份数量.py
from typing import List


class Solution:

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        city_number = len(isConnected)
        index = 0
        cities = [0] * city_number
        for i in range(city_number):
            if cities[i] == 0:
                index += 1
                cities[i] = index
                queue = []
                queue.append(i)
                while len(queue) != 0:
                    idx = queue.pop()
                    for j in range(city_number):
                        if isConnected[idx][j] == 1 and cities[j] == 0:
                            cities[j] = index
                            queue.append(j)
        return index


if __name__ == "__main__":
    s = Solution()
    print(s.findCircleNum(isConnected=[[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
