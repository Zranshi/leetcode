package main

func MaxInt(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func findMaxConsecutiveOnes(nums []int) int {
	idx, res := 0, 0
	for _, x := range nums {
		if x == 1 {
			idx++
		} else {
			res = MaxInt(res, idx)
			idx = 0
		}
	}
	return MaxInt(res, idx)
}
