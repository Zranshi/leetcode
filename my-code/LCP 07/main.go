package main

import "fmt"

// @Time     : 2021/7/1 09:24
// @Author   : Ranshi
// @File     : main.go

func numWays(n int, relation [][]int, k int) int {
	dp := make([]int, n)
	dp[0] = 1
	for i := 0; i < k; i++ {
		next := make([]int, n)
		for _, r := range relation {
			src, dst := r[0], r[1]
			next[dst] += dp[src]
		}
		dp = next
	}
	return dp[n-1]
}

func main() {
	n := 5
	relation := [][]int{
		{0, 2},
		{2, 1},
		{3, 4},
		{2, 3},
		{1, 4},
		{2, 0},
		{0, 4},
	}
	k := 3
	fmt.Println(numWays(n, relation, k))
}
