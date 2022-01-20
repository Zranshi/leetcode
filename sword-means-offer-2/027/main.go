package main

// @Time     : 2022/01/20 13:33
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 剑指 Offer II 027. 回文链表

import (
	"fmt"
	rs_type "leetcode/type"
)

type ListNode = rs_type.ListNode

func isPalindrome(head *ListNode) bool {
	fast, slow := head.Next, head
	for fast != nil && fast.Next != nil {
		fast = fast.Next.Next
		slow = slow.Next
	}
	newHead, p := &ListNode{}, slow.Next
	slow.Next = nil
	for p != nil {
		tmp := p.Next
		newHead.Next, p.Next = p, newHead.Next
		p = tmp
	}
	p1, p2 := head, newHead.Next
	for p1 != nil && p2 != nil {
		if p1.Val != p2.Val {
			return false
		}
		p1, p2 = p1.Next, p2.Next
	}
	return true
}

func main() {
	fmt.Println(isPalindrome(rs_type.ListNodeInitBySlice([]int{1, 1, 2, 1})))
}
