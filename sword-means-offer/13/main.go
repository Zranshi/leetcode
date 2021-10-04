package main

import "fmt"

// @Time     : 2021/10/05 07:46
// @Author   : Ranshi
// @File     : main.go

func digitSum(x, y int) int {
	res := 0
	for x != 0 {
		res += x % 10
		x /= 10
	}
	for y != 0 {
		res += y % 10
		y /= 10
	}
	return res
}

func movingCount(m int, n int, k int) (res int) {
	board := k + 1
	if k >= 8 {
		board = (k - 7) * 10
	}
	for i := 0; i < m; i++ {
		for j := 0; j < n && i+j < board; j++ {
			if digitSum(i, j) <= k {
				res++
			}
		}
	}
	return
}

func main() {
	fmt.Println(movingCount(2, 3, 1))
}
