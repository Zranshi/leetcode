package main

import (
	"fmt"
)

// @Time     : 2022/2/9 10:38
// @Author   : rs
// @File     : main.go

func countKDifference(nums []int, k int) (ans int) {
	cnt := map[int]int{}
	for _, num := range nums {
		ans += cnt[num-k] + cnt[num+k]
		cnt[num]++
	}
	return ans
}

func main() {
	fmt.Println(countKDifference([]int{1, 2, 2, 1}, 1))
}
