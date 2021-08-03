package main

func MaxInt(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func findMaxAverage(nums []int, k int) float64 {
	res, idx, length := 0, 0, len(nums)
	for _, x := range nums[0:k] {
		res += x
	}
	ans := res
	for idx+k < length {
		ans = ans + nums[idx+k] - nums[idx]
		res = MaxInt(res, ans)
		idx++
	}
	return float64(res) / float64(k)
}
