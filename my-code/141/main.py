class ListNode:
    def __init__(self, _next: "ListNode", x):
        self.val = x
        self.next = _next


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        while head:
            if head.val is None:
                return True
            head.val = None
            head = head.next
        return False
