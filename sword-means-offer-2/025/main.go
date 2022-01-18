package main

// @Time     : 2022/01/12 13:01
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 剑指 Offer II 025. 链表中的两数相加

import (
	"fmt"
	rs_type "leetcode/type"
)

type ListNode = rs_type.ListNode

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	arrL1, arrL2 := []int{}, []int{}
	cur := l1
	for cur != nil {
		arrL1 = append(arrL1, cur.Val)
		cur = cur.Next
	}
	cur = l2
	for cur != nil {
		arrL2 = append(arrL2, cur.Val)
		cur = cur.Next
	}
	flag := 0
	idxL1, idxL2 := len(arrL1)-1, len(arrL2)-1
	head := ListNode{Val: 0, Next: nil}

	getNode := func(num1, num2 int) *ListNode {
		val := num1 + num2 + flag
		if val >= 10 {
			val -= 10
			flag = 1
		} else {
			flag = 0
		}
		return &ListNode{Val: val, Next: nil}
	}
	for idxL1 >= 0 && idxL2 >= 0 {
		node := getNode(arrL1[idxL1], arrL2[idxL2])
		head.Next, node.Next = node, head.Next
		idxL1, idxL2 = idxL1-1, idxL2-1
	}
	for idxL1 >= 0 {
		node := getNode(arrL1[idxL1], 0)
		head.Next, node.Next = node, head.Next
		idxL1--
	}
	for idxL2 >= 0 {
		node := getNode(0, arrL2[idxL2])
		head.Next, node.Next = node, head.Next
		idxL2--
	}
	if flag == 1 {
		node := &ListNode{Val: 1, Next: nil}
		head.Next, node.Next = node, head.Next
	}
	return head.Next
}

func main() {
	fmt.Println(
		addTwoNumbers(
			rs_type.ListNodeInitBySlice([]int{9, 1, 6}),
			rs_type.ListNodeInitBySlice([]int{0}),
		))
}
