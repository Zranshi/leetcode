# -*- coding: UTF-8 -*-
# @Time     : 2024/01/18 20:13
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 42. 接雨水


class Solution:
    def trap(self, height: list[int]) -> int:
        pre_height = [0 for _ in range(len(height))]
        post_height = [0 for _ in range(len(height))]
        pre_height[0] = height[0]
        for i in range(1, len(height)):
            pre_height[i] = max(height[i], pre_height[i - 1])
        post_height[-1] = height[-1]
        for i in range(len(height) - 2, -1, -1):
            post_height[i] = max(height[i], post_height[i + 1])
        res = 0
        for i in range(len(height)):
            res += min(pre_height[i], post_height[i]) - height[i]
        return res


if __name__ == "__main__":
    print(Solution().trap(height=[4, 2, 0, 3, 2, 5]))
