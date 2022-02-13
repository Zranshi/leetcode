# -*- coding:utf-8 -*-
# @Time     : 2022/2/7 09:50
# @Author   : rs
# @File     : main.py
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        ans = []
        cnt = [[a, 'a'], [b, 'b'], [c, 'c']]
        while True:
            cnt.sort(key=lambda x: -x[0])
            has_next = False
            for i, (c, ch) in enumerate(cnt):
                if c <= 0:
                    break
                if len(ans) >= 2 and ans[-2] == ch and ans[-1] == ch:
                    continue
                has_next = True
                ans.append(ch)
                cnt[i][0] -= 1
                break
            if not has_next:
                return ''.join(ans)


if __name__ == '__main__':
    print(Solution().longestDiverseString(a=1, b=1, c=7))
