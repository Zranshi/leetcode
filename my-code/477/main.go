package main

func totalHammingDistance(nums []int) (res int) {
	length := len(nums)
	for i := 0; i < 30; i++ {
		c := 0
		for _, val := range nums {
			c += val >> i & 1
		}
		res += c * (length - c)
	}
	return
}
