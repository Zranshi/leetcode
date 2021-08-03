package main

func longestOnes(A []int, K int) int {
	left, right, idx := 0, 0, 0
	for right = 0; right < len(A); right++ {
		idx += 1 - A[right]
		if idx > K {
			idx -= 1 - A[left]
			left++
		}
	}
	return right - left
}
