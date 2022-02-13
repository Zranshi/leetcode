# -*- coding: UTF-8 -*-
# @Time     : 2021/09/24 07:37
# @Author   : Ranshi
# @File     : 123.py
class Node(object):
    def __init__(self, val, prev: "Node", next: "Node", child: "Node") -> None:
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: "Node") -> "Node":
        def dfs(node: "Node") -> "Node":
            cur = node
            last = None
            while cur:
                nxt = cur.next
                if cur.child:
                    child_last = dfs(cur.child)

                    nxt = cur.next
                    cur.next = cur.child
                    cur.child.prev = cur

                    if nxt:
                        child_last.next = nxt
                        nxt.prev = child_last

                    cur.child = None
                    last = child_last
                else:
                    last = cur
                cur = nxt

            return last

        dfs(head)
        return head
