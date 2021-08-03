# -*- coding:utf-8 -*-
# @Time     : 2021/6/28 13: 06
# @Author   : Ranshi
# @File     : 面试题 02.03. 删除中间节点.py
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, _next: Optional['ListNode'] = None):
        self.val = val
        self.next = _next


class Solution:
    def deleteNode(self, node: Optional[ListNode]):
        if node and node.next:
            node.val, node.next = node.next.val, node.next.next
