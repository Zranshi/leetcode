package main

// @Time     : 2022/01/11 20:58
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 剑指 Offer II 022. 链表中环的入口节点

import (
	rs_type "leetcode/type"
)

type ListNode = rs_type.ListNode

func detectCycle(head *ListNode) *ListNode {
	fast, slow := head, head
	for {
		if fast == nil || fast.Next == nil {
			return nil
		}
		fast, slow = fast.Next.Next, slow.Next
		if fast == slow {
			break
		}
	}
	fast = head
	for fast != slow {
		fast, slow = fast.Next, slow.Next
	}
	return fast
}
