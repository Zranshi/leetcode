package main

import (
	"fmt"
	rstype "leetcode/type"
)

type TreeNode = rstype.TreeNode

func replaceValueInTree(root *TreeNode) *TreeNode {
	if root == nil {
		return nil
	}
	levelSum := []int{0}
	var recordSum, replaceTree func(*TreeNode, int)
	recordSum = func(tn *TreeNode, i int) {
		if len(levelSum) < i+1 {
			levelSum = append(levelSum, 0)
		}
		levelSum[i] += tn.Val
		if tn.Left != nil {
			recordSum(tn.Left, i+1)
		}
		if tn.Right != nil {
			recordSum(tn.Right, i+1)
		}
	}
	replaceTree = func(tn *TreeNode, i int) {
		sum := 0
		if tn.Left != nil {
			sum += tn.Left.Val
			replaceTree(tn.Left, i+1)
		}
		if tn.Right != nil {
			sum += tn.Right.Val
			replaceTree(tn.Right, i+1)
		}
		if tn.Left != nil {
			tn.Left.Val = levelSum[i+1] - sum
		}
		if tn.Right != nil {
			tn.Right.Val = levelSum[i+1] - sum
		}
	}
    root.Val = 0
	recordSum(root, 0)
    replaceTree(root, 0)
	return root
}

func main() {
	tree := (*TreeNode)(rstype.TreeNodeInitBySlice([]int{5, 4, 9, 1, 10, 0, 7}))
	fmt.Println(replaceValueInTree(tree))
}
