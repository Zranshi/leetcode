package main

import "fmt"

type Node struct {
	Val         bool
	IsLeaf      bool
	TopLeft     *Node
	TopRight    *Node
	BottomLeft  *Node
	BottomRight *Node
}

func construct(grid [][]int) *Node {
	var dfs func(int, int, int, int) *Node
	dfs = func(top, buttom, left, right int) *Node {
		val := grid[top][left]
		flag := true
		for i := top; i < buttom; i++ {
			for j := left; j < right; j++ {
				if grid[i][j] != val {
					flag = false
					break
				}
			}
		}
		if flag {
			return &Node{
				Val:    val == 1,
				IsLeaf: true,
			}
		}
		rowMid, colMid := (top+buttom)/2, (left+right)/2
		return &Node{Val: true,
			IsLeaf:      false,
			TopLeft:     dfs(top, rowMid, left, colMid),
			TopRight:    dfs(top, rowMid, colMid, right),
			BottomLeft:  dfs(rowMid, buttom, left, colMid),
			BottomRight: dfs(rowMid, buttom, colMid, right),
		}
	}
	return dfs(0, len(grid), 0, len(grid[0]))
}

func main() {
	fmt.Println(construct([][]int{
		{1, 1, 1, 1, 0, 0, 0, 0},
		{1, 1, 1, 1, 0, 0, 0, 0},
		{1, 1, 1, 1, 1, 1, 1, 1},
		{1, 1, 1, 1, 1, 1, 1, 1},
		{1, 1, 1, 1, 0, 0, 0, 0},
		{1, 1, 1, 1, 0, 0, 0, 0},
		{1, 1, 1, 1, 0, 0, 0, 0},
		{1, 1, 1, 1, 0, 0, 0, 0},
	}))
}
