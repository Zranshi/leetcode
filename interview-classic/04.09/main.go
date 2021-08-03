package main

// @Time     : 2021/7/7 20:33
// @Author   : Ranshi
// @File     : main.go

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func BSTSequences(root *TreeNode) [][]int {
	if root == nil {
		return [][]int{{}}
	}
	var (
		res  [][]int
		path []int
		dfs  func(idx *TreeNode)
	)
	que := map[*TreeNode]bool{root: true}
	dfs = func(idx *TreeNode) {
		delete(que, idx)
		path = append(path, idx.Val)
		if idx.Left != nil {
			que[idx.Left] = true
			defer delete(que, idx.Left)
		}
		if idx.Right != nil {
			que[idx.Right] = true
			defer delete(que, idx.Right)
		}
		if len(que) == 0 {
			newSlice := make([]int, len(path))
			copy(newSlice, path)
			res = append(res, newSlice)
		} else {
			st := make([]*TreeNode, 0, len(que))
			for key := range que {
				st = append(st, key)
			}
			for i := range st {
				dfs(st[i])
			}
		}
		que[idx] = false
		path = path[:len(path)-1]
		return
	}
	dfs(root)
	return res
}

func main() {

}
