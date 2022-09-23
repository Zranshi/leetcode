package main

import "fmt"

// @Time     : 2022/09/22 16:06
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 1640. 能否连接形成数组

func canFormArray(arr []int, pieces [][]int) bool {
	index := make(map[int]int, len(pieces))
	for i, p := range pieces {
		index[p[0]] = i
	}
	for i := 0; i < len(arr); {
		if j, ok := index[arr[i]]; !ok {
			return false
		} else {
			for _, x := range pieces[j] {
				if arr[i] != x {
					return false
				}
				i++
			}
		}
	}
	return true
}

func main() {
	fmt.Println(canFormArray([]int{15, 88}, [][]int{{88}, {15}}))
}
