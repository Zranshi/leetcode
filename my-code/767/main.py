# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 14
# @Author   : Ranshi
# @File     : 767. 重构字符串.py
class Solution:
    def reorganizeString(self, S: str) -> str:
        cnt = [0 for i in range(26)]
        maxs = 0
        for i in S:
            cnt[ord(i) - ord("a")] += 1
            maxs = max(maxs, cnt[ord(i) - ord("a")])
        if maxs > (len(S) + 1) // 2:
            return ""
        import heapq

        heap = []
        ans = ""
        for i in range(26):
            if cnt[i] != 0:
                heapq.heappush(heap, [-cnt[i], i])
        while len(heap):
            cnts1, idx1 = heapq.heappop(heap)
            ans = ans + chr(idx1 + ord("a"))
            if len(heap) == 0:
                break
            cnts2, idx2 = heapq.heappop(heap)
            ans = ans + chr(idx2 + ord("a"))
            if cnts1 + 1 != 0:
                heapq.heappush(heap, [cnts1 + 1, idx1])
            if cnts2 + 1 != 0:
                heapq.heappush(heap, [cnts2 + 1, idx2])
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.reorganizeString(S="aab"))
