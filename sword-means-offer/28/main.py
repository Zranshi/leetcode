# -*- coding: UTF-8 -*-
# @Time     : 2021/09/28 22:38
# @Author   : Ranshi
# @File     : 123.py
from type.tree_node import TreeNode


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        que = [root]
        while que:
            for i in range(len(que) // 2):
                left, right = que[i], que[-(i + 1)]
                if (
                    left
                    and right
                    and left.val != right.val
                    or (not left or not right)
                    and (left or right)
                ):
                    return False
            new_que = []
            for item in que:
                if item:
                    new_que.append(item.left)
                    new_que.append(item.right)
            que = new_que
        return True


if __name__ == "__main__":
    print(Solution().isSymmetric(TreeNode.init_by_list([1, 2, 2, None, 3, None, 3])))
