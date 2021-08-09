package main

import "fmt"

// @Time     : 2021/08/08 11:55
// @Author   : Ranshi
// @File     : main.go

func searchMatrix(matrix [][]int, target int) bool {
	row, col := len(matrix), len(matrix[0])
	x, y := 0, col-1
	for {
		if matrix[x][y] == target {
			return true
		} else if matrix[x][y] > target {
			y--
		} else {
			x++
		}
		if y < 0 || x >= row {
			break
		}
	}
	return false
}

func main() {
	fmt.Println(searchMatrix([][]int{
		{1, 4, 7, 11, 15},
		{2, 5, 8, 12, 19},
		{3, 6, 9, 16, 22},
		{10, 13, 14, 17, 24},
		{18, 21, 23, 26, 30},
	}, 5))
}
