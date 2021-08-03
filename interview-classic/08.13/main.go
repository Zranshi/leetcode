package main

import (
	"fmt"
	"sort"
)

// @Time     : 2021/7/22 20:40
// @Author   : Ranshi
// @File     : main.go

func pileBox(box [][]int) int {
	boxLen := len(box)
	if boxLen == 0 {
		return 0
	}
	sort.Slice(box, func(i, j int) bool {
		return box[i][0] < box[j][0]
	})
	dp, res := make([]int, boxLen), box[0][2]
	dp[0] = box[0][2]
	for i := 1; i < boxLen; i++ {
		dp[i] = box[i][2]
		for j := 0; j < i; j++ {
			if box[i][0] > box[j][0] && box[i][1] > box[j][1] && box[i][2] > box[j][2] {
				dp[i] = max(dp[i], dp[j]+box[i][2])
			}
		}
		res = max(res, dp[i])
	}
	return res
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func main() {
	fmt.Println(pileBox([][]int{
		{1, 1, 1},
		{2, 3, 4},
		{2, 6, 7},
		{3, 4, 5},
	}))
}
