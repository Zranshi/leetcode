package main

// @Time     : 2021/08/03 20:33
// @Author   : Ranshi
// @File     : main.go

type ListNode struct {
	Val  int
	Next *ListNode
}

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
	l := &ListNode{
		Val:  0,
		Next: nil,
	}
	removeNthFromEnd(l, 8)
}
