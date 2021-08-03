# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 01
# @Author   : Ranshi
# @File     : 145. 二叉树的后序遍历.py
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def post(root: TreeNode):
            if not root:
                return
            post(root.left)
            post(root.right)
            res.append(root.val)

        res = []
        post(root)
        return res
