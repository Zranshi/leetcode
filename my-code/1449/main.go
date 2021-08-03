package main

import "math"

// @Time     : 2021/6/12 09:22
// @Author   : Ranshi
// @File     : 1449. 数位成本和为目标值的最大数字.go

func MaxInt(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func largestNumber1(cost []int, target int) string {
	dp := make([]int, target+1)
	for i := range dp {
		dp[i] = math.MinInt32
	}
	dp[0] = 0
	for _, c := range cost {
		for j := c; j <= target; j++ {
			dp[j] = MaxInt(dp[j], dp[j-c]+1)
		}
	}
	if dp[target] < 0 {
		return "0"
	}
	ans := make([]byte, 0, dp[target])
	for i, j := 8, target; i >= 0; i-- {
		for c := cost[i]; j >= c && dp[j] == dp[j-c]+1; j -= c {
			ans = append(ans, byte('1'+i))
		}
	}
	return string(ans)
}
