package main

// @Time     : 2021/6/4 13:55
// @Author   : Ranshi
// @File     : 剑指 Offer 06. 从尾到头打印链表.go

type ListNode struct {
	Val  int
	Next *ListNode
}

func reversePrint(head *ListNode) (ans []int) {
	cur := head
	for cur != nil {
		ans = append(ans, cur.Val)
		cur = cur.Next
	}
	for i, j := 0, len(ans)-1; i < j; i, j = i+1, j-1 {
		ans[i], ans[j] = ans[j], ans[i]
	}
	return
}

func main() {
}
