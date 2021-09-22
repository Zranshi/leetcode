# -*- coding: UTF-8 -*-
# @Time     : 2021/09/22 20:53
# @Author   : Ranshi
# @File     : main.py
from type.tree_node import TreeNode


class Node(TreeNode):
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        super.__init__(val, left, right)
        self.next = next


class Solution:
    def connect(self, root: "Node") -> "Node":
        if not root:
            return root
        que = [root]
        while que:
            pre = que[0]
            for i in range(len(que)):
                temp = que.pop(0)
                if temp.left:
                    que.append(temp.left)
                if temp.right:
                    que.append(temp.right)
                if i != 0:
                    pre.next = temp
                    pre = temp
        return root


if __name__ == "__main__":
    print(Solution().connect(Node.init_by_list([1, 2, None, 4, 5])))
