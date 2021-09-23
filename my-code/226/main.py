# -*- coding: UTF-8 -*-
# @Time     : 2021/09/05 23:31
# @Author   : Ranshi
# @File     : main.py
from type.tree_node import TreeNode


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        else:
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root


if __name__ == "__main__":
    print(Solution().invertTree(TreeNode.init_by_list([4, 2, 7, 1, 3, 6, 9, 10])))
