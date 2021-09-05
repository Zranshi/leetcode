# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 17: 58
# @Author   : Ranshi
# @File     : 94. 二叉树的中序遍历.py
from typing import List
from type.tree_node import TreeNode


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def inorder(root: TreeNode):
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)

        res = []
        inorder(root)
        return res
