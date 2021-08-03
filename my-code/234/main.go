package main

// @Time     : 2021/5/30 10:19
// @Author   : Ranshi
// @File     : 234. 回文链表.go

type ListNode struct {
	Val  int
	Next *ListNode
}

func isPalindrome(head *ListNode) bool {
	if head == nil || head.Next == nil {
		return true
	}
	slow, fast := head, head
	var pre *ListNode
	for fast != nil && fast.Next != nil {
		fast = fast.Next.Next
		slow.Next, pre, slow = pre, slow, slow.Next
	}
	if fast != nil {
		slow = slow.Next
	}
	for slow != nil && pre != nil {
		if slow.Val != pre.Val {
			return false
		}
		slow = slow.Next
		pre = pre.Next
	}
	return true
}
