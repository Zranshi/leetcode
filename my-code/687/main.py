# -*- coding: UTF-8 -*-
# @Time     : 2022/09/02 10:01
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 687. 最长同值路径

from type.tree_node import TreeNode


class Solution:
    def longestUnivaluePath(self, root: None | TreeNode) -> int:
        ans = 0

        def dfs(node: TreeNode | None) -> int:
            if node is None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            left1 = left + 1 if node.left and node.left.val == node.val else 0
            right1 = right + 1 if node.right and node.right.val == node.val else 0
            nonlocal ans
            ans = max(ans, left1 + right1)
            return max(left1, right1)

        dfs(root)
        return ans


if __name__ == "__main__":
    print(Solution().longestUnivaluePath(TreeNode.init_by_list([5, 4, 5, 1, 1, 5])))
