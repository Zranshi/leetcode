package rstype

import (
	"strconv"
	"strings"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func TreeNodeInitBySlice(lst []int) *TreeNode {
	idx := 0
	var recFun func([]int, int) *TreeNode
	recFun = func(lst []int, idx int) *TreeNode {
		if idx < len(lst) && lst[idx] != 0 {
			return &TreeNode{
				Val:   lst[idx],
				Left:  recFun(lst, idx*2+1),
				Right: recFun(lst, idx*2+2),
			}
		}
		return nil
	}
	return recFun(lst, idx)
}

func (tn *TreeNode) String() string {
	if tn == nil {
		return ""
	}
	var res []string
	level := []*TreeNode{tn}
	flag := true
	for flag {
		flag = false
		var nextLevel []*TreeNode
		var idxStr []string
		for _, node := range level {
			if node == nil {
				idxStr = append(idxStr, "nil")
			} else {
				flag = true
				idxStr = append(idxStr, strconv.Itoa(node.Val))
				nextLevel = append(nextLevel, node.Left)
				nextLevel = append(nextLevel, node.Right)
			}
		}
		res = append(res, strings.Join(idxStr, " "))
		level = nextLevel
	}
	return strings.Join(res[:len(res)-1], "\n")
}
