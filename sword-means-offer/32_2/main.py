# -*- coding: UTF-8 -*-
# @Time     : 2021/09/28 07:46
# @Author   : Ranshi
# @File     : 123.py
from typing import List

from type.tree_node import TreeNode


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        que = [root]
        res = []
        while que:
            new_que = []
            res.append([item.val for item in que])
            for item in que:
                if item.left:
                    new_que.append(item.left)
                if item.right:
                    new_que.append(item.right)
            que = new_que
        return res


if __name__ == "__main__":
    print(Solution().levelOrder(TreeNode.init_by_list([3, 9, 20, None, None, 15, 7])))
