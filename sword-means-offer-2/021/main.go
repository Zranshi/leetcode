package main

// @Time     : 2022/01/11 18:31
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 剑指 Offer II 021. 删除链表的倒数第 n 个结点
import (
	"fmt"
	rs_type "leetcode/type"
)

type ListNode = rs_type.ListNode

func removeNthFromEnd(head *ListNode, n int) *ListNode {
	newHead := &ListNode{Val: 0, Next: head}
	fast, slow := newHead, newHead
	for fast.Next != nil {
		if n != 0 {
			n--
		} else {
			slow = slow.Next
		}
		fast = fast.Next
	}
	slow.Next = slow.Next.Next
	return newHead.Next
}

func main() {
	fmt.Println(removeNthFromEnd(rs_type.ListNodeInitBySlice([]int{1}), 1))
}
