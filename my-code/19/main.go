package main

// @Time     : 2021/08/03 20:33
// @Author   : Ranshi
// @File     : main.go

import (
	"fmt"
	rs_type "leetcode/type"
)

type ListNode = rs_type.ListNode

func removeNthFromEnd(head *ListNode, n int) *ListNode {
	linkHead := &ListNode{
		Val:  0,
		Next: head,
	}
	fast, slow := linkHead, linkHead
	for fast.Next != nil {
		if n != 0 {
			n--
		} else {
			slow = slow.Next
		}
		fast = fast.Next
	}
	slow.Next = slow.Next.Next
	return linkHead.Next
}

func main() {
	fmt.Println(removeNthFromEnd(rs_type.ListNodeInitBySlice([]int{1}), 1))
}
