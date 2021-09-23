# -*- coding:utf-8 -*-
# @Time     : 2021/7/27 08:57
# @Author   : Ranshi
# @File     : main.py
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        _min: int = root.val
        res = float("inf")
        stk = [root]
        while stk:
            idx = stk.pop()
            if idx.val != _min and idx.val < res:
                res = idx.val
            if idx.left and idx.right:
                stk.append(idx.right)
                stk.append(idx.left)
        return res if res != float("inf") else -1
