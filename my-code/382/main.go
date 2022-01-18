package main

// @Time     : 2022/01/16 10:35
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 382. 链表随机节点
import (
	rs_type "leetcode/type"
	"math/rand"
)

type ListNode = rs_type.ListNode

type Solution struct {
	Head *ListNode
}

func Constructor(head *ListNode) Solution {
	return Solution{
		Head: head,
	}
}

func (s *Solution) GetRandom() (ans int) {
	for node, i := s.Head, 1; node != nil; node, i = node.Next, i+1 {
		if rand.Intn(i) == 0 {
			ans = node.Val
		}
	}
	return
}
