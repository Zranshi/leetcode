# -*- coding:utf-8 -*-
# @Time     : 2021/5/19 14:01
# @Author   : Ranshi
# @File     : 111. 二叉树的最小深度.py
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        from collections import deque

        if not root:
            return 0
        de = deque()
        de.append([root, 1])
        while len(de):
            cur, h = de.popleft()
            if cur.left or cur.right:
                if cur.left:
                    de.append([cur.left, h + 1])
                if cur.right:
                    de.append([cur.right, h + 1])
            else:
                return h
