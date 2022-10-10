package main

import (
	"fmt"
	rs_type "leetcode/type"
)

// @Time     : 2022/10/08 15:20
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 剑指 Offer II 050. 向下的路径节点之和

type TreeNode = rs_type.TreeNode

func pathSum(root *TreeNode, targetSum int) (ans int) {
	if root == nil {
		return
	}
	lst := []int{}
	var dfs func(*TreeNode)
	dfs = func(tn *TreeNode) {
		lst = append(lst, tn.Val)
		pre := make([]int, len(lst)+1)
		for i := 0; i < len(lst); i++ {
			pre[i+1] = pre[i] + lst[i]
		}
		for i := 0; i < len(pre)-1; i++ {
			if pre[len(pre)-1]-pre[i] == targetSum {
				ans++
			}
		}
		if tn.Left != nil {
			dfs(tn.Left)
		}
		if tn.Right != nil {
			dfs(tn.Right)
		}
		lst = lst[:len(lst)-1]
	}
	dfs(root)
	return
}

func main() {
	fmt.Println(pathSum(rs_type.TreeNodeInitBySlice([]int{10, 5, -3, 3, 2, 0, 11, 3, -2, 0, 1}), 8))
}
