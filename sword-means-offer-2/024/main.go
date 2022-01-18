package main

// @Time     : 2022/01/12 10:42
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 剑指 Offer II 024. 反转链表
import (
	"fmt"
	rs_type "leetcode/type"
)

type ListNode = rs_type.ListNode

func reverseList(head *ListNode) *ListNode {
	newHead := ListNode{Val: 0, Next: nil}
	cur := head
	for cur != nil {
		next := cur.Next
		newHead.Next, cur.Next = cur, newHead.Next
		cur = next
	}
	return newHead.Next
}

func main() {
	fmt.Println(reverseList(rs_type.ListNodeInitBySlice([]int{1, 2, 3, 4, 5})))
}
