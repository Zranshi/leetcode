package main

import (
	"fmt"
	"sort"
)

// @Time     : 2022/09/14 00:37
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 1619. 删除某些元素后的数组均值

func trimMean(arr []int) (ans float64) {
	cnt, length := 0, len(arr)
	sort.Ints(arr)
	for i := length / 20; i < length-length/20; i++ {
		ans += float64(arr[i])
		cnt += 1
	}
	return ans / float64(cnt)
}

func main() {
	fmt.Println(trimMean([]int{6, 0, 7, 0, 7, 5, 7, 8, 3, 4, 0, 7, 8, 1, 6, 8, 1, 1, 2, 4, 8, 1, 9, 5, 4, 3, 8, 5, 10, 8, 6, 6, 1, 0, 6, 10, 8, 2, 3, 4}))
}
