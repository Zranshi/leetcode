package main

// @Time     : 2022/09/15 20:33
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 剑指 Offer II 029. 排序的循环链表

type Node struct {
	Val  int
	Next *Node
}

func insert(head *Node, x int) *Node {
	if head == nil {
		node := &Node{Val: x}
		node.Next = node
		return node
	}
	pre, node := head, &Node{Val: x}
	for {
		if pre.Val <= x && x <= pre.Next.Val || (pre.Next.Val < pre.Val && (x >= pre.Val || x <= pre.Next.Val)) || pre.Next == head {
			pre.Next, node.Next = node, pre.Next
			break
		}
		pre = pre.Next
	}
	return head
}
