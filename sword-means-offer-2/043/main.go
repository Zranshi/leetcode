package main

import (
	"fmt"
	rs_type "leetcode/type"
)

type TreeNode = rs_type.TreeNode

// @Time     : 2022/09/16 22:56
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 剑指 Offer II 043. 往完全二叉树添加节点

type CBTInserter struct {
	que []int
}

func Constructor(root *TreeNode) CBTInserter {
	nodeSlice := []*TreeNode{root}
	ci := CBTInserter{que: []int{root.Val}}
	for len(nodeSlice) != 0 {
		nextLevel := []*TreeNode{}
		for _, node := range nodeSlice {
			if node.Left != nil {
				nextLevel = append(nextLevel, node.Left)
				ci.que = append(ci.que, node.Left.Val)
			}
			if node.Right != nil {
				nextLevel = append(nextLevel, node.Right)
				ci.que = append(ci.que, node.Right.Val)
			}
		}
		nodeSlice = nextLevel
	}
	return ci
}

func (ci *CBTInserter) Insert(v int) int {
	ci.que = append(ci.que, v)
	return ci.que[len(ci.que)/2-1]
}

func (ci *CBTInserter) Get_root() *TreeNode {
	var dfs func(int) *TreeNode
	dfs = func(i int) *TreeNode {
		if i >= len(ci.que) {
			return nil
		}
		return &TreeNode{
			Val:   ci.que[i],
			Left:  dfs(i*2 + 1),
			Right: dfs(i*2 + 2),
		}
	}
	return dfs(0)
}

func main() {
	root := rs_type.TreeNodeInitBySlice([]int{1, 2, 3, 4, 5, 6})
	ci := Constructor(root)
	fmt.Println(ci.que)
	fmt.Println(ci.Insert(7))
	fmt.Println(ci.Get_root())
}
