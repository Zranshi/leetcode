package main

import (
	"fmt"
	rstype "leetcode/type"
)

type ListNode = rstype.ListNode

func insertionSortList(head *ListNode) *ListNode {
	headNode := &ListNode{Next: head}
	cur := headNode.Next
	for cur.Next != nil {
		idx := cur.Next
		if idx.Val >= cur.Val {
			cur = cur.Next
			continue
		}
		cur.Next = cur.Next.Next
		insertCur := headNode
		for insertCur != cur {
			if insertCur.Next.Val > idx.Val {
				idx.Next = insertCur.Next
				insertCur.Next = idx
				break
			}
			insertCur = insertCur.Next
		}
	}
	return headNode.Next
}

func main() {
	fmt.Println(insertionSortList(rstype.ListNodeInitBySlice([]int{1, 1})))
}
