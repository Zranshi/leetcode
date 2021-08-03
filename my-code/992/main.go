package main

func subarraysWithKDistinct(A []int, K int) int {
	if A == nil || len(A) < K {
		return 0
	}
	hash := make([]int, len(A)+1)
	l, count, result, results := 0, 0, 1, 0
	for r := 0; r < len(A); r++ {
		hash[A[r]]++

		if hash[A[r]] == 1 {
			count++
		}
		for hash[A[l]] > 1 || count > K {
			if count > K {
				result = 1
				count--
			} else {
				result++
			}
			hash[A[l]]--
			l++
		}
		if count == K {
			results += result
		}
	}
	return results
}
