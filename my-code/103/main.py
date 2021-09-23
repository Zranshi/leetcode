# -*- coding: UTF-8 -*-
# @Time     : 2021/08/19 08:26
# @Author   : Ranshi
# @File     : main.py

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        from collections import deque

        if not root:
            return []
        result = []
        que = deque()
        que.append(root)
        k = 0
        while que:
            tmp = []
            k += 1
            for i in range(len(que)):
                node = que.popleft()
                if k % 2 != 0:
                    tmp.append(node.val)
                else:
                    tmp.insert(0, node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            result.append(tmp)
        return result


if __name__ == "__main__":
    ...
