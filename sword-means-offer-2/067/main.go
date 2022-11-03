package main

import (
	"fmt"
)

// @Time     : 2022/11/03 23:22
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 剑指 Offer II 067. 最大的异或

func findMaximumXOR(nums []int) (ans int) {
	const highBit = 30
	for k := highBit; k >= 0; k-- {
		seen := map[int]bool{}
		for _, v := range nums {
			seen[v>>k] = true
		}

		xNext := ans*2 + 1
		found := false

		for _, v := range nums {
			if seen[v>>k^xNext] {
				found = true
				break
			}
		}

		if found {
			ans = xNext
		} else {
			ans = xNext - 1
		}
	}
    return
}

func main() {
	fmt.Println(findMaximumXOR([]int{3, 10, 5, 25, 2, 8}))
}
