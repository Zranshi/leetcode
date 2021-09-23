# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 17: 59
# @Author   : Ranshi
# @File     : 112. 路径总和.py
from type.tree_node import TreeNode


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return targetSum == root.val
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(
            root.right, targetSum - root.val
        )
