# -*- coding: UTF-8 -*-
# @Time     : 2021/12/25 21:02
# @Author   : Ranshi
# @File     : 123.py
# @Doc      : 1609. 奇偶树
from typing import Optional

from pyal.container import TreeNode


class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        level = 0
        level_node = [root]
        while level_node:
            next_level_node = []
            flag = float("inf") if level % 2 else 0
            for node in level_node:
                if (
                    ((node.val + level) % 2 == 0)
                    or (level % 2 == 0 and flag >= node.val)
                    or (level % 2 == 1 and flag <= node.val)
                ):
                    return False
                flag = node.val
                if node.left:
                    next_level_node.append(node.left)
                if node.right:
                    next_level_node.append(node.right)
            level_node = next_level_node
            level += 1
        return True


if __name__ == "__main__":
    print(Solution().isEvenOddTree(root=TreeNode.init_by_lst([5, 4, 2, 3, 3, 7])))
