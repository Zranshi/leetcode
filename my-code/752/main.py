# -*- coding:utf-8 -*-
# @Time     : 2021/6/25 09: 11
# @Author   : Ranshi
# @File     : 752. 打开转盘锁.py
from typing import List


class Solution:
    def openLock(self, arr: List[str], target: str) -> int:
        from collections import deque
        dq, path, error_state, res, target = deque(), {0}, set([int(item) for item in arr]), 0, int(target)
        dq.appendleft((0, 0))

        def next_state(n: int, mark: int, flag: int) -> int:
            if flag == 1 and n // (10 ** mark) % 10 == 0:
                return n + 9 * (10 ** mark)
            elif flag == 0 and n // (10 ** mark) % 10 == 9:
                return n - 9 * (10 ** mark)
            else:
                return n + (10 ** mark) if flag == 0 else n - (10 ** mark)

        while dq:
            idx, res = dq[-1]
            if idx in error_state:
                dq.pop()
                continue
            elif idx == target:
                break
            for i in range(8):
                pos, ori = i // 2, i % 2
                x = next_state(idx, pos, ori)
                if x not in path:
                    path.add(x)
                    dq.appendleft((x, res + 1))
            dq.pop()

        return res if dq else -1


if __name__ == '__main__':
    s = Solution()
    print(s.openLock(["0201", "0101", "0102", "1212", "2002"]
                     , "0202"))
