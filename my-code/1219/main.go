package main

import "fmt"

// @Time     : 2022/02/05 17:36
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 1219. 黄金矿工

var dirs = []struct{ x, y int }{
	{-1, 0},
	{1, 0},
	{0, -1},
	{0, 1},
}

func getMaximumGold(grid [][]int) (ans int) {
	var dfs func(x, y, gold int)
	dfs = func(x, y, gold int) {
		gold += grid[x][y]
		if ans < gold {
			ans = gold
		}
		tmp := grid[x][y]
		grid[x][y] = 0
		for _, d := range dirs {
			nx, ny := x+d.x, y+d.y
			if 0 <= nx && nx < len(grid) && 0 <= ny && ny < len(grid[0]) && grid[nx][ny] > 0 {
				dfs(nx, ny, gold)
			}
		}
		grid[x][y] = tmp
	}
	for i, row := range grid {
		for j, gold := range row {
			if gold > 0 {
				dfs(i, j, 0)
			}
		}
	}
	return
}

func main() {
	fmt.Println(getMaximumGold([][]int{
		{1, 0, 7},
		{2, 0, 6},
		{3, 4, 5},
		{0, 3, 0},
		{9, 0, 20},
	}))
}
