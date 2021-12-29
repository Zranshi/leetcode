package main

import "fmt"

// @Time     : 2021/12/14 22:33
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 剑指 Offer II 004. 只出现一次的数字

func singleNumber(nums []int) (ans int) {
	set := make(map[int]int)
	for _, v := range nums {
		set[v]++
	}
	for key, val := range set {
		if val == 1 {
			ans = key
		}
	}
	return
}

func main() {
	fmt.Println(singleNumber([]int{0, 1, 0, 1, 0, 1, 100}))
}
