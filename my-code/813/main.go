package main

// @Time     : 2021/6/1 20:29
// @Author   : Ranshi
// @File     : 813. 最大平均值和的分组.go

func MaxFloat64(f float64, f2 float64) float64 {
	if f > f2 {
		return f
	}
	return f2
}

func largestSumOfAverages(nums []int, k int) float64 {
	preSum := []int{0}
	for i := range nums {
		preSum = append(preSum, preSum[len(preSum)-1]+nums[i])
	}
	average := func(left, right int) float64 {
		return float64(preSum[right]-preSum[left]) / float64(right-left)
	}
	length := len(nums)
	var dp []float64
	for i := range nums {
		dp = append(dp, average(i, length))
	}
	if len(dp) == 0 {
		return 0
	}
	for _k := 0; _k < k-1; _k++ {
		for i := 0; i < length; i++ {
			for j := i + 1; j < length; j++ {
				dp[i] = MaxFloat64(dp[i], average(i, j)+dp[j])
			}
		}
	}
	return dp[0]
}
