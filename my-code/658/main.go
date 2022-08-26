package main

import (
	"fmt"
	"sort"
)

// @Time     : 2022/08/25 03:11
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 658. 找到 K 个最接近的元素

func findClosestElements(arr []int, k int, x int) []int {
	right := sort.SearchInts(arr, x)
	left := right - 1
	for ; k > 0; k-- {
		if left < 0 {
			right++
		} else if right >= len(arr) || x-arr[left] <= arr[right]-x {
			left--
		} else {
			right++
		}
	}
	return arr[left+1 : right]
}

func main() {
	fmt.Println(findClosestElements([]int{1, 2, 3, 4, 5}, 4, 3))
}
