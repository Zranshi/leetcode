package main

// @Time     : 2021/6/29 20:33
// @Author   : Ranshi
// @File     : main.go

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

type ListNode struct {
	Val  int
	Next *ListNode
}

func listOfDepth(tree *TreeNode) (res []*ListNode) {
	queueTree := []*TreeNode{tree}
	lengthTree := []int{tree.Val}
	levelLength := 0
	cur := &ListNode{}

	for len(queueTree) != 0 {
		idx := queueTree[0]
		idxLength := lengthTree[0]

		if idxLength != levelLength {
			levelLength = idxLength
			res = append(res, &ListNode{
				Val:  idx.Val,
				Next: nil,
			})
			cur = res[len(res)-1]
		} else {
			cur.Next = &ListNode{
				Val:  idx.Val,
				Next: nil,
			}
			cur = cur.Next
		}

		if idx.Left != nil {
			queueTree = append(queueTree, idx.Left)
			lengthTree = append(lengthTree, idxLength+1)
		}
		if idx.Right != nil {
			queueTree = append(queueTree, idx.Right)
			lengthTree = append(lengthTree, idxLength+1)
		}
		queueTree = queueTree[1:]
		lengthTree = lengthTree[1:]
	}
	return
}
