# -*- coding: UTF-8 -*-
# @Time     : 2021/09/28 07:50
# @Author   : Ranshi
# @File     : 123.py
from typing import List
from type.tree_node import TreeNode


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        from collections import deque

        if not root:
            return []
        res, queue = [], deque()
        queue.append(root)
        while queue:
            tmp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(tmp[::-1] if len(res) % 2 else tmp)
        return res


if __name__ == "__main__":
    print(Solution().levelOrder(TreeNode.init_by_list([3, 9, 20, None, None, 15, 7])))
