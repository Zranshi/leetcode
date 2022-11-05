package main

import (
	"fmt"
	"sort"
)

// @Time     : 2022/11/05 12:48
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 剑指 Offer II 069. 山峰数组的顶部

func peakIndexInMountainArray(arr []int) int {
	return sort.Search(len(arr)-1, func(i int) bool { return arr[i] > arr[i+1] })
}

func main() {
	fmt.Println(peakIndexInMountainArray([]int{3, 5, 3, 2, 0}))
}
