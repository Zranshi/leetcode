package main

import "fmt"

func maxResult(nums []int, k int) int {
	dp := make([]int, len(nums))
    dp[0] = nums[0]
	queue := []int{0}
	for i := 1; i < len(nums); i++ {
        for len(queue) > 0 && i-queue[0] > k {
            queue = queue[1:]
        }
		dp[i] = dp[queue[0]] + nums[i]
        for len(queue) > 0 && dp[queue[len(queue)-1]] <= dp[i] {
            queue = queue[:len(queue)-1]
        }
		queue = append(queue, i)
	}
	return dp[len(dp)-1]
}

func main() {
	fmt.Println(maxResult([]int{10, -5, -2, 4, 0, 3}, 3))
}
