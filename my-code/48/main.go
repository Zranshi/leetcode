package main

import "fmt"

// @Time     : 2021/08/07 13:16
// @Author   : Ranshi
// @File     : main.go

func rotate(matrix [][]int) {
	row, col := 0, 0
	if len(matrix)%2 == 0 {
		row, col = len(matrix)/2, len(matrix)/2
	} else {
		row, col = len(matrix)/2, len(matrix)/2+1
	}
	for i := 0; i < row; i++ {
		for j := 0; j < col; j++ {
			idx := matrix[i][j]
			for k := 0; k < 4; k++ {
				i, j = j, len(matrix)-i-1
				idx, matrix[i][j] = matrix[i][j], idx
			}
		}
	}
}

func main() {
	nums := [][]int{
		{1, 2, 3},
		{4, 5, 6},
		{7, 8, 9},
	}
	rotate(nums)
	fmt.Println(nums)
}
