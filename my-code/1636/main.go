package main

import (
	"fmt"
	"sort"
)

// @Time     : 2022/09/19 16:05
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 1636. 按照频率将数组升序排序

func frequencySort(nums []int) (ans []int) {
	couter := map[int]int{}
	for _, v := range nums {
		couter[v] += 1
	}
	couterList := [][]int{}
	for i, v := range couter {
		couterList = append(couterList, []int{i, v})
	}
	sort.Slice(couterList, func(i, j int) bool {
		if couterList[i][1] == couterList[j][1] {
			return couterList[i][0] > couterList[j][0]
		}
		return couterList[i][1] < couterList[j][1]
	})
	for _, v := range couterList {
		for i := 0; i < v[1]; i++ {
			ans = append(ans, v[0])
		}
	}
	return ans
}

func main() {
	fmt.Println(frequencySort([]int{-1, 1, -6, 4, 5, -6, 1, 4, 1}))
}
