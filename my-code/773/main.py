# -*- coding:utf-8 -*-
# @Time     : 2021/6/26 08: 23
# @Author   : Ranshi
# @File     : 773. 滑动谜题.py
from typing import List, Tuple


class Solution:
    move_map = {"LEFT": 1, "RIGHT": -1, "UP": 3, "DOWN": -3}

    def slidingPuzzle(self, board: List[List[int]]) -> int:
        from collections import deque

        def get_start() -> Tuple[int, int]:
            idx, res, f = 5, 0, 0
            for item in board:
                for x in item:
                    if x == 0:
                        f = idx
                    res += x * (10 ** idx)
                    idx -= 1
            return f, res

        def get_next_state(idx: int, f: int, m: str) -> Tuple[int, int]:
            swap = f + self.move_map[m]
            swap_num = idx // (10 ** swap) % 10
            res = 0
            if 0 <= swap <= 5:
                res = idx + swap_num * (10 ** f - 10 ** swap)
            return swap, res

        path_set = set()
        flag, start = get_start()
        dq = deque()
        path = 0
        dq.appendleft((flag, start, 0))
        while dq:
            idx_flag, idx_state, path = dq[-1]
            if idx_state == 123450:
                break
            for move in self.move_map:
                next_flag, next_state = get_next_state(idx_state, idx_flag, move)
                if next_state != 0 and next_state not in path_set:
                    path_set.add(next_state)
                    dq.appendleft((next_flag, next_state, path + 1))
            dq.pop()
        return path if dq else -1


if __name__ == "__main__":
    s = Solution()
    print(s.slidingPuzzle([[3, 2, 4], [1, 5, 0]]))
