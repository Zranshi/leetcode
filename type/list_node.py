# -*- coding: UTF-8 -*-
# @Time     : 2021/09/02 10:05
# @Author   : Ranshi
# @File     : listNode.py
# @Doc      : ListNode类
from typing import Optional


class ListNode(object):
    def __init__(self, val=0, _next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = _next

    def __str__(self) -> str:
        res_lst = []
        cur = self
        while cur:
            res_lst.append(str(cur.val))
            cur = cur.next
        return " -> ".join(res_lst)

    @classmethod
    def init_by_lst(cls, lst: list) -> Optional["ListNode"]:
        head = ListNode(val=-1, _next=None)
        cur = head
        for v in lst:
            cur.next = ListNode(val=v, _next=None)
            cur = cur.next
        return head.next
