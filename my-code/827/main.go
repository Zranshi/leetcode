package main

import "fmt"

// @Time     : 2022/09/18 16:10
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 827. 最大人工岛

func largestIsland(grid [][]int) (ans int) {
	dir4 := []struct{ x, y int }{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}
	n, t := len(grid), 0
	tag := make([][]int, n)
	for i := range tag {
		tag[i] = make([]int, n)
	}
	area := map[int]int{}
	var dfs func(int, int)
	dfs = func(i, j int) {
		tag[i][j] = t
		area[t]++
		for _, d := range dir4 {
			x, y := i+d.x, j+d.y
			if 0 <= x && x < n && 0 <= y && y < n && grid[x][y] > 0 && tag[x][y] == 0 {
				dfs(x, y)
			}
		}
	}
	for i, row := range grid {
		for j, x := range row {
			if x > 0 && tag[i][j] == 0 { // 枚举没有访问过的陆地
				t = i*n + j + 1
				dfs(i, j)
				ans = max(ans, area[t])
			}
		}
	}

	for i, row := range grid {
		for j, x := range row {
			if x == 0 { // 枚举可以添加陆地的位置
				newArea := 1
				conn := map[int]bool{0: true}
				for _, d := range dir4 {
					x, y := i+d.x, j+d.y
					if 0 <= x && x < n && 0 <= y && y < n && !conn[tag[x][y]] {
						newArea += area[tag[x][y]]
						conn[tag[x][y]] = true
					}
				}
				ans = max(ans, newArea)
			}
		}
	}
	return
}

func max(a, b int) int {
	if b > a {
		return b
	}
	return a
}

func main() {
	fmt.Println(largestIsland([][]int{
		{1, 0},
		{0, 1},
	}))
}
