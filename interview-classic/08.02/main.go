package main

import "fmt"

// @Time     : 2021/7/19 21:29
// @Author   : Ranshi
// @File     : main.go
func pathWithObstacles(obstacleGrid [][]int) [][]int {
	var (
		ans [][]int
		row = len(obstacleGrid) - 1
		col = len(obstacleGrid[0]) - 1
		dfs func([][]int)
	)
	dfs = func(path [][]int) {
		if len(ans) == 0 {
			i, j := path[len(path)-1][0], path[len(path)-1][1]
			if obstacleGrid[i][j] == 0 {
				obstacleGrid[i][j] = 1
				if j < col {
					dfs(append(path, []int{i, j + 1}))
				}
				if i < row {
					dfs(append(path, []int{i + 1, j}))
				}
				if i == row && j == col {
					ans = make([][]int, row+col+1)
					copy(ans, path)
				}
			}
		}
	}
	dfs([][]int{{0, 0}})
	return ans
}

func main() {
	fmt.Println(pathWithObstacles([][]int{
		{0, 0, 0},
		{0, 1, 0},
		{0, 0, 0},
	}))
}
