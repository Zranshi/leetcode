package main

import "fmt"

// @Time     : 2022/08/24 22:44
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 1460. 通过翻转子数组使两个数组相等

func canBeEqual(target []int, arr []int) bool {
	targetDict := make(map[int]int)
	arrDict := make(map[int]int)
	for _, v := range target {
		targetDict[v]++
	}
	for _, v := range arr {
		arrDict[v]++
	}
	for k, v := range targetDict {
		if _, has := arrDict[k]; !has || arrDict[k] != v {
			return false
		}
	}
	return true
}

func main() {
	fmt.Println(canBeEqual([]int{1, 2, 3, 4}, []int{2, 4, 1, 3}))
}
