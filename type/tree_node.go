package rs_type

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func TreeNodeInitBySlice(lst []int, idx int) *TreeNode {
	if idx < len(lst) && lst[idx] != 0 {
		return &TreeNode{
			Val:   lst[idx],
			Left:  TreeNodeInitBySlice(lst, idx*2+1),
			Right: TreeNodeInitBySlice(lst, idx*2+2),
		}
	}
	return nil
}
