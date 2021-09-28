# -*- coding: UTF-8 -*-
# @Time     : 2021/09/28 06:58
# @Author   : Ranshi
# @File     : main.py
from type.tree_node import TreeNode


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        def rootSum(root, targetSum):
            if root is None:
                return 0

            ret = 0
            if root.val == targetSum:
                ret += 1

            ret += rootSum(root.left, targetSum - root.val)
            ret += rootSum(root.right, targetSum - root.val)
            return ret

        if root is None:
            return 0

        ret = rootSum(root, targetSum)
        ret += self.pathSum(root.left, targetSum)
        ret += self.pathSum(root.right, targetSum)
        return ret


if __name__ == "__main__":
    print(
        Solution().pathSum(
            TreeNode.init_by_list([1, -2, -3, 1, 3, -2, None, -1]),
            targetSum=-1,
        )
    )
