package main

import "fmt"

func uniquePathsWithObstacles(obstacleGrid [][]int) int {
	row, col := len(obstacleGrid), len(obstacleGrid[0])
	if obstacleGrid[0][0] == 1 {
		return 0
	}
	mark := make([][]int, row)
	for i := 0; i < row; i++ {
		mark[i] = make([]int, col)
	}
	mark[0][0] = 1
	for i := 0; i < row; i++ {
		for j := 0; j < col; j++ {
			if obstacleGrid[i][j] == 1 {
				continue
			}
			if i > 0 {
				mark[i][j] += mark[i-1][j]
			}
			if j > 0 {
				mark[i][j] += mark[i][j-1]
			}
		}
	}
	return mark[row-1][col-1]
}

func main() {
	fmt.Println(uniquePathsWithObstacles([][]int{
		{0, 0, 0},
		{0, 1, 0},
		{0, 0, 0},
	}))
}
