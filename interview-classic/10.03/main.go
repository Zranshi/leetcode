package main

import (
	"fmt"
)

// @Time     : 2021/7/22 20:48
// @Author   : Ranshi
// @File     : main.go

func search(arr []int, target int) int {
	for i := range arr {
		if arr[i] == target {
			return i
		}
	}
	return -1
}

func main() {
	fmt.Println(search([]int{15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14}, 5))
}
