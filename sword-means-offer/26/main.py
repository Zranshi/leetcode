# -*- coding: UTF-8 -*-
# @Time     : 2021/09/28 21:56
# @Author   : Ranshi
# @File     : main.py
from type.tree_node import TreeNode


class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def recur(A, B):
            if not B:
                return True
            if not A or A.val != B.val:
                return False
            return recur(A.left, B.left) and recur(A.right, B.right)

        return bool(A and B) and (
            recur(A, B)
            or self.isSubStructure(A.left, B)
            or self.isSubStructure(A.right, B)
        )


if __name__ == "__main__":
    print(
        Solution().isSubStructure(
            A=TreeNode.init_by_list([3, 4, 5, 1, 2]),
            B=TreeNode.init_by_list([4, 1]),
        )
    )
