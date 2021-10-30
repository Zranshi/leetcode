# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 17: 58
# @Author   : Ranshi
# @File     : 100. 相同的树.py
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if (q and not p) or (not q and p):
            return False
        elif not q and not p:
            return True
        else:
            if p.val == q.val:
                return (
                    True and self.isSameTree(q.right, p.right) and self.isSameTree(q.left, p.left)
                )
            return False
