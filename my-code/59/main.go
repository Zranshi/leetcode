package main

import "fmt"

// @Time     : 2021/08/07 13:33
// @Author   : Ranshi
// @File     : main.go

func generateMatrix(n int) [][]int {
	x, y, nextFlag := 0, 0, 0
	nextPath := [][]int{{0, 1}, {1, 0}, {0, -1}, {-1, 0}}
	res := make([][]int, n)
	for i := 0; i < n; i++ {
		res[i] = make([]int, n)
	}
	for idx := 1; idx <= n*n; idx++ {
		res[x][y] = idx
		nextX, nextY := x+nextPath[nextFlag][0], y+nextPath[nextFlag][1]
		if 0 <= nextX && nextX < n && 0 <= nextY && nextY < n && res[nextX][nextY] == 0 {
			x, y = nextX, nextY
		} else {
			nextFlag = (nextFlag + 1) % 4
			x, y = x+nextPath[nextFlag][0], y+nextPath[nextFlag][1]
		}
	}
	return res
}

func main() {
	fmt.Println(generateMatrix(4))
}
