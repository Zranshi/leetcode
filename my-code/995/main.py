# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 18
# @Author   : Ranshi
# @File     : 995. K 连续位的最小翻转次数.py
import collections


class Solution():
    def minKBitFlips(self, A, K):
        length, res, que = len(A), 0, collections.deque()
        for i in range(length):
            if que and i >= que[0] + K:
                que.popleft()
            if len(que) % 2 == A[i]:
                if i + K > length:
                    return -1
                que.append(i)
                res += 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.minKBitFlips(A=[1, 1, 0], K=2))
