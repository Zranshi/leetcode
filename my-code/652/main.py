# -*- coding: UTF-8 -*-
# @Time     : 2022/09/05 10:53
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 652. 寻找重复的子树

from typing import Optional

from type.tree_node import TreeNode


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> list[Optional[TreeNode]]:
        seen = {}
        idx = 0
        repeat = set()

        def dfs(node: TreeNode):
            if not node:
                return 0
            tri = node.val, dfs(node.left), dfs(node.right)
            if tri in seen:
                tree, index = seen[tri]
                repeat.add(tree)
                return index
            else:
                nonlocal idx
                idx += 1
                seen[tri] = (node, idx)
                return idx

        dfs(root)
        return list(repeat)


if __name__ == "__main__":
    print(
        Solution().findDuplicateSubtrees(
            TreeNode.init_by_list([1, 2, 3, 4, None, 2, 4, None, None, 4])
        )
    )
