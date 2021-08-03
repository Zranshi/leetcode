package main

import (
	"fmt"
	"sort"
)

// @Time     : 2021/7/15 21:43
// @Author   : Ranshi
// @File     : main.go

func maximumElementAfterDecrementingAndRearranging(arr []int) int {
	n := len(arr)
	sort.Ints(arr)
	arr[0] = 1
	for i := 1; i < n; i++ {
		arr[i] = min(arr[i], arr[i-1]+1)
	}
	return arr[n-1]
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func main() {
	fmt.Println(maximumElementAfterDecrementingAndRearranging([]int{2, 2, 1, 2, 1}))
}
