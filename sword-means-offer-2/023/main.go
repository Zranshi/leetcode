package main

// @Time     : 2022/01/11 21:03
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 剑指 Offer II 023. 两个链表的第一个重合节点

import rs_type "leetcode/type"

type ListNode = rs_type.ListNode

func getIntersectionNode(headA, headB *ListNode) *ListNode {
	if headA == nil || headB == nil {
		return nil
	}
	pa, pb := headA, headB
	for pa != pb {
		if pa == nil {
			pa = headB
		} else {
			pa = pa.Next
		}
		if pb == nil {
			pb = headA
		} else {
			pb = pb.Next
		}
	}
	return pa
}
