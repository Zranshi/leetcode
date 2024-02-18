package main

import "fmt"

func maxProfit(prices []int) int {
	days := len(prices)
	dp := make([][3]int, days)
	dp[0][0] = -prices[0]
	for i := 1; i < days; i++ {
		// dp[i][0] 表示当前持有股票的最大收益. dp[i-1][0] 表示前一天持有并且不卖出, 所以等于不改变; dp[i-1][2]-prices[i] 表示前一天不持有并且不在冷冻期, 所以收益要减去购买股票的开销.
		dp[i][0] = max(dp[i-1][0], dp[i-1][2]-prices[i])
		// dp[i][1] 表示当前不持有股票, 并且处于冷冻期的最大累计收益. 最大收益即为前一天持有股票后的收益加上这一天股票的价格.
		dp[i][1] = dp[i-1][0] + prices[i]
		// dp[i][2] 表示当前不持有股票, 并且不处于冷冻期的最大累计收益. 最大收益等于前一天在与不在冷冻期的收益的最大值.
		dp[i][2] = max(dp[i-1][1], dp[i-1][2])
	}
	return max(dp[days-1][1], dp[days-1][2])
}

func main() {
	fmt.Println(maxProfit([]int{1, 2, 3, 0, 2}))
}
