package rs_type

import (
	"strconv"
	"strings"
)

type ListNode struct {
	Val  int
	Next *ListNode
}

func ListNodeInitBySlice(lst []int) *ListNode {
	head := &ListNode{Val: -1, Next: nil}
	cur := head
	for _, v := range lst {
		cur.Next = &ListNode{Val: v, Next: nil}
		cur = cur.Next
	}
	return head.Next
}

func (ln *ListNode) String() string {
	res := []string{}
	cur := ln
	for cur != nil {
		res = append(res, strconv.Itoa(cur.Val))
		cur = cur.Next
	}
	return strings.Join(res, " -> ")
}
