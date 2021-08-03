package main

// @Time     : 2021/5/30 20:49
// @Author   : Ranshi
// @File     : 237. 删除链表中的节点.go

type ListNode struct {
	Val  int
	Next *ListNode
}

func deleteNode(node *ListNode) {
	node.Val = node.Next.Val
	node.Next = node.Next.Next
}
