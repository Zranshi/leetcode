package main

import "fmt"

// @Time     : 2021/08/04 10:09
// @Author   : Ranshi
// @File     : main.go

func maxAreaOfIsland(grid [][]int) (res int) {
	row, col := len(grid), len(grid[0])
	path := make([]bool, row*col)
	next_path := [][]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
	for idx := 0; idx < row*col; idx++ {
		idx_r, idx_c := idx/col, idx%col
		// 如果已经搜索过，则进入下一次循环
		if path[idx] || grid[idx_r][idx_c] == 0 {
			continue
		}
		// 如果当前是岛的一部分，则宽度优先搜索这个岛，并将所有岛的区域加入到以搜索集合
		dq := [][]int{{idx_r, idx_c}}
		area := 0
		for len(dq) != 0 {
			cur_r, cur_c := dq[0][0], dq[0][1]
			path[idx] = true
			area += 1
			for _, next := range next_path {
				next_r, next_c := cur_r+next[0], cur_c+next[1]
				if 0 <= next_r && next_r < row && 0 <= next_c && next_c < col && grid[next_r][next_c] == 1 && !path[next_r*col+next_c] {
					path[next_r*col+next_c] = true
					dq = append(dq, []int{next_r, next_c})
				}
			}
			dq = dq[1:]
		}
		if res < area {
			res = area
		}
	}
	return
}

func main() {
	fmt.Println(maxAreaOfIsland([][]int{
		{0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0},
		{0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0},
		{0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0},
		{0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0},
		{0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0},
		{0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0},
		{0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0},
		{0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0},
	}))
}
