package main

// @Time     : 2021/6/30 13:47
// @Author   : Ranshi
// @File     : main.go

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func inorderSuccessor(root *TreeNode, p *TreeNode) *TreeNode {
	var (
		treeNodes []*TreeNode
		inOrder   func(node *TreeNode)
	)
	inOrder = func(r *TreeNode) {
		if r != nil {
			inOrder(r.Left)
			treeNodes = append(treeNodes, r)
			inOrder(r.Right)
		}
	}
	inOrder(root)
	for i := range treeNodes {
		if treeNodes[i] == p {
			if i == len(treeNodes)-1 {
				return nil
			} else {
				return treeNodes[i+1]
			}
		}
	}
	return nil
}
