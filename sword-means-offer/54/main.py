#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/10/07 15:50
# @Author   : Ranshi
# @File     : main.py
from type.tree_node import TreeNode


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        def dfs(root):
            if not root:
                return
            dfs(root.right)
            if self.k == 0:
                return
            self.k -= 1
            if self.k == 0:
                self.res = root.val
            dfs(root.left)

        self.k = k
        dfs(root)
        return self.res


if __name__ == "__main__":
    print(
        Solution().kthLargest(
            root=TreeNode.init_by_list([3, 1, 4, None, 2]),
            k=1,
        )
    )
