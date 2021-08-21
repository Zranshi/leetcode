package main

// @Time     : 2021/08/21 08:02
// @Author   : Ranshi
// @File     : main.go

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func kthSmallest(t *TreeNode, k int) int {
	sorted := []int{}
	var inorder func(t *TreeNode)
	inorder = func(t *TreeNode) {
		if t != nil {
			inorder(t.Left)
			sorted = append(sorted, t.Val)
			inorder(t.Right)
		}
	}
	inorder(t)
	return sorted[k-1]
}

func main() {

}
