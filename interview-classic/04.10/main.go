package main

// @Time     : 2021/7/8 20:12
// @Author   : Ranshi
// @File     : main.go

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func checkSubTree(t1 *TreeNode, t2 *TreeNode) (res bool) {
	var (
		check func(node1, node2 *TreeNode) bool
		dfs   func(node *TreeNode)
	)
	check = func(node1, node2 *TreeNode) bool {
		if node1 == nil && node2 == nil {
			return true
		} else if node1 == nil || node2 == nil || node1.Val != node2.Val {
			return false
		}
		return check(node1.Left, node2.Left) && check(node1.Right, node2.Right)
	}
	dfs = func(node *TreeNode) {
		if node != nil {
			if node.Val == t2.Val {
				res = check(node, t2)
				if res {
					return
				}
			}
			dfs(node.Left)
			dfs(node.Right)
		}
	}
	dfs(t1)
	return
}

func main() {

}
