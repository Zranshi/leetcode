# -*- coding:utf-8 -*-
# @Time     : 2021/7/3 22: 56
# @Author   : Ranshi
# @File     : 123.py
# class TreeNode:
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        if not root:
            return None
        root_l = []

        def get_pre(idx: TreeNode):
            root_l.append(idx)
            if idx.left:
                get_pre(idx.left)
            if idx.right:
                get_pre(idx.right)

        get_pre(root)
        for i in range(len(root_l) - 1):
            root_l[i].right = root_l[i + 1]
            root_l[i].left = None
