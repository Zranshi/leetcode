# -*- coding: UTF-8 -*-
# @Time     : 2021/09/05 06:40
# @Author   : Ranshi
# @File     : 123.py


from typing import List
from type.tree_node import TreeNode


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        from collections import deque

        level_node: List[List[str]] = [[]]
        dq = deque([(root, 0)])
        while dq:
            idx, idx_level = dq.pop()
            if idx_level >= len(level_node):
                level_node.append([])
            if idx:
                level_node[idx_level].append(idx.val)
                dq.appendleft((idx.left, idx_level + 1))
                dq.appendleft((idx.right, idx_level + 1))
        return level_node[:-1]


if __name__ == "__main__":
    print(Solution().levelOrder(TreeNode.init_by_list([3, 9, 20, None, None, 15, 7])))
