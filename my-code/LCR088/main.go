package main

import "fmt"

func min(x, y int) int {
	if x > y {
		return y
	}
	return x
}

func minCostClimbingStairs(cost []int) int {
	dp := make([]int, len(cost)+1)
	for i := 2; i < len(dp); i++ {
		dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
	}
	return dp[len(dp)-1]
}

func main() {
	fmt.Println(minCostClimbingStairs([]int{10, 15, 20}))
}
