package main

import (
	"fmt"
	"sort"
)

// @Time     : 2021/08/08 12:12
// @Author   : Ranshi
// @File     : main.go

func eraseOverlapIntervals(intervals [][]int) int {
	n := len(intervals)
	if n == 0 {
		return 0
	}
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i][1] < intervals[j][1]
	})
	ans, right := 1, intervals[0][1]
	for _, p := range intervals[1:] {
		if p[0] >= right {
			ans++
			right = p[1]
		}
	}
	return n - ans
}

func main() {
	fmt.Println(eraseOverlapIntervals([][]int{
		{1, 2},
		{2, 3},
		{3, 4},
		{1, 3},
	}))
}
