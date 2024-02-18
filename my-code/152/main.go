package main

import "fmt"

func maxProduct(nums []int) int {
	maxF, minF, ans := nums[0], nums[0], nums[0]
	for i := 1; i < len(nums); i++ {
		mx, mn := maxF, minF
		maxF = max(mx*nums[i], mn*nums[i], nums[i])
		minF = min(mx*nums[i], mn*nums[i], nums[i])
		ans = max(maxF, ans)
	}
	return ans
}

func main() {
	fmt.Println(maxProduct([]int{2, 3, -2, 4}))
}
