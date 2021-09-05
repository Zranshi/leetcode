# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 01
# @Author   : Ranshi
# @File     : 145. 二叉树的后序遍历.py
from typing import List
from type.tree_node import TreeNode


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
