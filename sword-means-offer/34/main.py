#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/10/07 14:51
# @Author   : Ranshi
# @File     : main.py

from typing import List
from type.tree_node import TreeNode
from collections import defaultdict, deque


class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        ret = []
        parent = defaultdict(lambda: None)

        def getPath(node: TreeNode):
            tmp = []
            while node:
                tmp.append(node.val)
                node = parent[node]
            ret.append(tmp[::-1])

        if not root:
            return ret

        que_node = deque([root])
        que_total = deque([0])

        while que_node:
            node = que_node.popleft()
            rec = que_total.popleft() + node.val

            if not node.left and not node.right:
                if rec == target:
                    getPath(node)
            else:
                if node.left:
                    parent[node.left] = node
                    que_node.append(node.left)
                    que_total.append(rec)
                if node.right:
                    parent[node.right] = node
                    que_node.append(node.right)
                    que_total.append(rec)

        return ret


if __name__ == "__main__":
    print(
        Solution().pathSum(
            root=TreeNode.init_by_list(
                [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]
            ),
            target=22,
        )
    )
