package main

// @Time     : 2021/5/30 09:08
// @Author   : Ranshi
// @File     : 206. 反转链表.go

type ListNode struct {
	Val  int
	Next *ListNode
}

// 头节点插入法
func _reverseList(head *ListNode) *ListNode {
	if head == nil {
		return nil
	}
	newHead := &ListNode{}
	for head.Next != nil {
		next := head.Next
		head.Next = newHead.Next
		newHead.Next = head
		head = next
	}
	head.Next = newHead.Next
	return head
}

func reverseList(head *ListNode) *ListNode {
	var prev *ListNode
	curr := head
	for curr != nil {
		curr.Next, prev, curr = prev, curr, curr.Next
	}
	return prev
}
