package main

func hammingWeight(num uint32) (res int) {
	for i := 0; i < 32; i++ {
		if 1<<i&num > 0 {
			res++
		}
	}
	return
}
