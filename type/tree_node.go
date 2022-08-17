package rs_type

import (
	"fmt"
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
	res := []string{}
	level := []*TreeNode{tn}
	flag := true
	for flag {
		flag = false
		levelRes := make([]string, len(level))
		nextLevel := make([]*TreeNode, len(level)*2)
		for i, v := range level {
			if v != nil {
				flag = true
				levelRes[i] = fmt.Sprintf(" %5v ", v.Val)
				nextLevel[i*2] = v.Left
				nextLevel[i*2+1] = v.Right
			} else {
				levelRes[i] = " nil "
				nextLevel[i*2] = nil
				nextLevel[i*2+1] = nil
			}
		}
		res = append(res, strings.Join(levelRes, " "))
	}
	return strings.Join(res, "\n")
}
