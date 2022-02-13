# -*- coding: UTF-8 -*-
# @Time     : 2021/09/05 06:53
# @Author   : Ranshi
# @File     : 123.py

from typing import List
from type.tree_node import TreeNode


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        from collections import deque

        level_node: List[List[str]] = [[]]
        dq = deque([(root, 0)])
        while dq:
            idx, idx_level = dq.pop()
            if idx_level >= len(level_node):
                cur = level_node[-1]
                for i in range(len(cur)):
                    if cur[i] != cur[-i - 1]:
                        return False
                level_node.append([])
            if idx:
                level_node[idx_level].append(idx.val)
                dq.appendleft((idx.left, idx_level + 1))
                dq.appendleft((idx.right, idx_level + 1))
            else:
                level_node[idx_level].append(None)
        return True


if __name__ == "__main__":
    print(Solution().isSymmetric(TreeNode.init_by_list([1, 2, 2, 3, 4, 4, 3])))
