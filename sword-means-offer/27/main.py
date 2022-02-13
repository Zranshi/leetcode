# -*- coding: UTF-8 -*-
# @Time     : 2021/09/28 22:30
# @Author   : Ranshi
# @File     : 123.py
from type.tree_node import TreeNode


class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        return (
            (
                TreeNode(
                    val=root.val,
                    left=self.mirrorTree(root.right),
                    right=self.mirrorTree(root.left),
                )
            )
            if root
            else None
        )


if __name__ == "__main__":
    print(Solution().mirrorTree(TreeNode.init_by_list([4, 2, 7, 1, 3, 6, 9])))
