package main

import (
	"fmt"
	"sort"
)

// @Time     : 2021/08/06 09:35
// @Author   : Ranshi
// @File     : main.go

type SortBy [][]int

func (a SortBy) Len() int      { return len(a) }
func (a SortBy) Swap(i, j int) { a[i], a[j] = a[j], a[i] }
func (a SortBy) Less(i, j int) bool {
	if a[i][0] == a[j][0] {
		return a[i][1] < a[j][1]
	} else {
		return a[i][0] < a[j][0]
	}
}

func merge(intervals [][]int) (res [][]int) {
	sort.Sort(SortBy(intervals))
	idxRange := intervals[0]
	for idx, item := range intervals {
		if idxRange[1] >= item[0] {
			if idxRange[1] <= item[1] {
				idxRange[1] = item[1]
			}
		} else {
			res = append(res, idxRange)
			idxRange = item
		}
		if idx == len(intervals)-1 {
			res = append(res, idxRange)
		}
	}
	return
}

func main() {
	fmt.Printf("%v\n", merge([][]int{
		{1, 4},
		{4, 5},
	}))
}
