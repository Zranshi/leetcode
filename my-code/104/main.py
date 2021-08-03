# -*- coding:utf-8 -*-
# @Time     : 2021/5/19 20:15
# @Author   : Ranshi
# @File     : 104. 二叉树的最大深度.py
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        from collections import deque
        if not root:
            return 0
        de = deque()
        de.append([root, 1])
        res = 0
        while len(de):
            idx, h = de.popleft()
            if idx.left or idx.right:
                if idx.left:
                    de.append([idx.left, h + 1])
                if idx.right:
                    de.append([idx.right, h + 1])
            else:
                res = res if res > h else h
        return res
