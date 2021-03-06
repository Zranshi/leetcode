# -*- coding: UTF-8 -*-
# @Time     : 2021/09/25 07:33
# @Author   : Ranshi
# @File     : 123.py
from typing import Optional

from type.list_node import ListNode


class Node(ListNode):
    def __init__(
        self,
        val=0,
        _next: Optional["ListNode"] = None,
        random: Optional["Node"] = None,
    ) -> None:
        super().__init__(val=val, next_=_next)
        self.random = random


class Solution:
    def copyRandomList(self, head: "Node") -> "Node":
        if not head:
            return
        cur = head
        # 1. 复制各节点，并构建拼接链表
        while cur:
            tmp = Node(cur.val)
            tmp.next = cur.next
            cur.next = tmp
            cur = tmp.next
        # 2. 构建各新节点的 random 指向
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        # 3. 拆分两链表
        cur = res = head.next
        pre = head
        while cur.next:
            pre.next = pre.next.next
            cur.next = cur.next.next
            pre = pre.next
            cur = cur.next
        pre.next = None  # 单独处理原链表尾节点
        return res  # 返回新链表头节点
