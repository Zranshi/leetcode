package main

import (
	"fmt"
	rs_type "leetcode/type"
)

// @Time     : 2022/10/14 21:04
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 剑指 Offer II 056. 二叉搜索树中两个节点之和

type TreeNode = rs_type.TreeNode

func findTarget(root *TreeNode, k int) bool {
	intMap := map[int]bool{}
	stk := []*TreeNode{root}
	for len(stk) != 0 {
		tn := stk[0]
		if _, ok := intMap[k-tn.Val]; ok {
			return true
		}
		intMap[tn.Val] = true
		if tn.Left != nil {
			stk = append(stk, tn.Left)
		}
		if tn.Right != nil {
			stk = append(stk, tn.Right)
		}
		stk = stk[1:]
	}
	return false
}

func main() {
	fmt.Println(findTarget(rs_type.TreeNodeInitBySlice([]int{8, 6, 10, 5, 7, 9, 11}), 12))
}
