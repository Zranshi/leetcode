package rs_type

type ListNode struct {
	Val  int
	Next *ListNode
}

func ListNodeInitBySlice(lst []int) *ListNode {
	head := &ListNode{Val: -1, Next: nil}
	cur := head
	for v := range lst {
		cur.Next = &ListNode{Val: v, Next: nil}
		cur = cur.Next
	}
	return head.Next
}
