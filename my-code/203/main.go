package main

// @Time     : 2021/5/30 08:51
// @Author   : Ranshi
// @File     : 203. 移除链表元素.go

type ListNode struct {
	Val  int
	Next *ListNode
}

// 我的想法
func _removeElements(head *ListNode, val int) *ListNode {
	if head == nil {
		return nil
	}
	for head.Val == val {
		if head.Next != nil {
			head = head.Next
		} else {
			return nil
		}
	}
	if head == nil {
		return nil
	}
	cur := head
	for cur.Next != nil {
		if cur.Next.Val == val {
			cur.Next = cur.Next.Next
		} else {
			cur = cur.Next
		}
	}
	return head
}

// 哨兵节点
func removeElements(head *ListNode, val int) *ListNode {
	newHead := &ListNode{}
	idx := newHead
	for head != nil {
		if head.Val != val {
			idx.Next = head
			idx = idx.Next
		}
		head = head.Next
	}
	idx.Next = nil
	return newHead.Next
}
