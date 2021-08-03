# -*- coding:utf-8 -*-
# @Time     : 2021/5/17 09:09
# @Author   : Ranshi
# @File     : 993. 二叉树的堂兄弟节点.py

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        from collections import deque
        x_pre, x_lev, y_pre, y_lev = 0, 0, 0, 0
        de = deque()
        de.append([root, 0])
        while len(de):
            cur, idx = de.popleft()
            if cur.left:
                if cur.left.val == x:
                    x_pre = cur
                    x_lev = idx + 1
                elif cur.left.val == y:
                    y_pre = cur
                    y_lev = idx + 1
                else:
                    de.append([cur.left, idx + 1])
            if cur.right:
                if cur.right.val == x:
                    x_pre = cur
                    x_lev = idx + 1
                elif cur.right.val == y:
                    y_pre = cur
                    y_lev = idx + 1
                else:
                    de.append([cur.right, idx + 1])
        return x_lev == y_lev and x_pre != y_pre
