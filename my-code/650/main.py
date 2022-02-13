# -*- coding: UTF-8 -*-
# @Time     : 2021/09/21 20:02
# @Author   : Ranshi
# @File     : 123.py
class Solution:
    def _minSteps(self, n: int) -> int:
        """
        动态规划 + bfs解法

        Args:
            n (int): 目标字符数

        Returns:
            int: 最小的操作数
        """
        from collections import deque

        if n == 1:
            return 0
        dp = [float("inf") for _ in range(n + 1)]
        dp[1], dp[2] = 0, 2
        dq = deque([(2, 1, 2)])
        while dq:
            idx, idx_path, idx_ope_num = dq.pop()
            dp[idx] = min(dp[idx], idx_ope_num)
            if idx == n:
                break
            if idx + idx_path <= n:
                dq.appendleft((idx + idx_path, idx_path, idx_ope_num + 1))
            if idx * 2 <= n:
                dq.appendleft((idx * 2, idx, idx_ope_num + 2))
        return dp[-1]

    def minSteps(self, n: int) -> int:
        f = [0] * (n + 1)
        for i in range(2, n + 1):
            f[i] = float("inf")
            j = 1
            while j * j <= i:
                if i % j == 0:
                    f[i] = min(f[i], f[j] + i // j)
                    f[i] = min(f[i], f[i // j] + j)
                j += 1

        return f[n]


if __name__ == "__main__":
    print(Solution().minSteps(3))
