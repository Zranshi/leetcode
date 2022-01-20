package main

// @Time     : 2022/01/20 13:02
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 剑指 Offer II 026. 重排链表

import (
	"fmt"
	rs_type "leetcode/type"
)

type ListNode = rs_type.ListNode

func reorderList(head *ListNode) {
	// 首先找到中间节点
	fast, mid := head, head
	for fast != nil && fast.Next != nil {
		fast = fast.Next.Next
		mid = mid.Next
	}
	// 然后将后半段链表逆序
	newHead := &ListNode{Val: 0, Next: nil}
	after := mid.Next
	mid.Next = nil
	for after != nil {
		tmp := after.Next
		newHead.Next, after.Next = after, newHead.Next
		after = tmp
	}
	// 将两个链表合并
	resHead := &ListNode{Val: 0, Next: nil}
	p := resHead
	p1, p2 := head, newHead.Next
	flag := true
	for p1 != nil && p2 != nil {
		if flag {
			p.Next, p1 = p1, p1.Next
			flag = false
		} else {
			p.Next, p2 = p2, p2.Next
			flag = true
		}
		p = p.Next
	}
	if p1 != nil {
		p.Next = p1
	}
	if p2 != nil {
		p.Next = p2
	}
}

func main() {
	ln := rs_type.ListNodeInitBySlice([]int{1, 2, 3, 4, 5, 6, 7, 8})
	fmt.Println(ln)
	reorderList(ln)
	fmt.Println(ln)
}
