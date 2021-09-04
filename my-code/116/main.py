# coding: utf-8
# @Time     : 2021/08/12 16:29
# @Author   : Ranshi
# @File     : main.py


class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: "Node") -> "Node":
        from collections import deque

        if not root:
            return root
        dq = deque([root])
        while dq:
            size = len(dq)
            for i in range(size):
                node = dq.pop()
                if i < size - 1:
                    node.next = dq[-1]
                if node.left:
                    dq.appendleft(node.left)
                if node.right:
                    dq.appendleft(node.right)
        return root


if __name__ == "__main__":
    ...
