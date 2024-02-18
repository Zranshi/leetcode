package main

type Node struct {
	Val      int
	Children []*Node
}

func levelOrder(root *Node) [][]int {
	if root == nil {
		return [][]int{}
	}
	res := make([][]int, 0)
	idxLevel := make([]*Node, 0)
	idxLevel = append(idxLevel, root)
	for len(idxLevel) != 0 {
		thisLevel := []int{}
		nextLevel := []*Node{}
		for _, n := range idxLevel {
			thisLevel = append(thisLevel, n.Val)
			nextLevel = append(nextLevel, n.Children...)
		}
		idxLevel = nextLevel
		res = append(res, thisLevel)
	}
	return res
}

func main() {
	levelOrder(nil)
}
