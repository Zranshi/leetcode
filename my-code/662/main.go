package main

import (
	"fmt"
	rs_type "leetcode/type"
)

// @Time     : 2022/08/27 00:50
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 662. 二叉树最大宽度

type TreeNode = rs_type.TreeNode

type pair struct {
	node  *TreeNode
	index int
}

func widthOfBinaryTree(root *TreeNode) int {
	ans := 1
	q := []pair{{root, 1}}
	for q != nil {
		ans = max(ans, q[len(q)-1].index-q[0].index+1)
		tmp := q
		q = nil
		for _, p := range tmp {
			if p.node.Left != nil {
				q = append(q, pair{p.node.Left, p.index * 2})
			}
			if p.node.Right != nil {
				q = append(q, pair{p.node.Right, p.index*2 + 1})
			}
		}
	}
	return ans
}

func max(a, b int) int {
	if b > a {
		return b
	}
	return a
}

func main() {
	fmt.Println(widthOfBinaryTree(rs_type.TreeNodeInitBySlice([]int{1, 3, 2, 5, 3, 0, 9})))
}
