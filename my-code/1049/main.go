package main

// @Time     : 2021/6/8 13:21
// @Author   : Ranshi
// @File     : 1049. 最后一块石头的重量 II.go
func lastStoneWeightII(stones []int) int {
	sum := 0
	for _, item := range stones {
		sum += item
	}
	m := sum / 2
	dp := make([]bool, m+1)
	dp[0] = true
	for _, weight := range stones {
		for j := m; j >= weight; j-- {
			dp[j] = dp[j] || dp[j-weight]
		}
	}
	for j := m; ; j-- {
		if dp[j] {
			return sum - 2*j
		}
	}
}
