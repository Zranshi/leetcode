# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 01
# @Author   : Ranshi
# @File     : 144. 二叉树的前序遍历.py
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def pre(root: TreeNode):
            if not root:
                return
            res.append(root.val)
            pre(root.left)
            pre(root.right)

        res = []
        pre(root)
        return res
