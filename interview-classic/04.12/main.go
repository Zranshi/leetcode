package main

// @Time     : 2021/7/16 21:00
// @Author   : Ranshi
// @File     : main.go

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func pathSum(root *TreeNode, sum int) int {
	var f func(*TreeNode, []int) int
	f = func(r *TreeNode, a []int) (result int) {
		if r != nil {
			s := make([]int, len(a)+1)
			copy(s, a)
			for i := range s {
				s[i] += r.Val
				if s[i] == sum {
					result++
				}
			}
			result += f(r.Left, s) + f(r.Right, s)
		}
		return
	}
	return f(root, []int{})
}

func main() {

}
