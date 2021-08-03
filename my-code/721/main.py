# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 13
# @Author   : Ranshi
# @File     : 721. 合并空间.py
class Solution:
    def merge(self, intervals):
        temp = sorted(intervals, key=lambda x: x[0])
        n = len(temp)
        if n < 2:
            return intervals
        cur = temp[0]
        res = []
        for elem in temp[1:]:
            if elem[0] > cur[1]:
                res.append(cur)
                cur = elem
            elif elem[1] > cur[1]:
                cur[1] = elem[1]
        res.append(cur)
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
