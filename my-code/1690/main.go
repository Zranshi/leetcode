package main

import "fmt"

func stoneGameVII(stones []int) int {
	n := len(stones)
	sum := make([]int, n+1)
	dp := make([][]int, n)

	for i := range dp {
		dp[i] = make([]int, n)
	}
	for i := 0; i < n; i++ {
		sum[i+1] = sum[i] + stones[i]
	}
	for i := n - 2; i >= 0; i-- {
		for j := i + 1; j < n; j++ {
			dp[i][j] = max(sum[j+1]-sum[i+1]-dp[i+1][j], sum[j]-sum[i]-dp[i][j-1])
		}
	}
	return dp[0][n-1]
}

func main() {
	fmt.Println(stoneGameVII([]int{7, 90, 5, 1, 100, 10, 10, 2}))
}

// 5 + 4 = 9
// 3 + 1 = 4

// 5
