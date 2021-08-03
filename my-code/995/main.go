package main

func minKBitFlips(A []int, K int) (ans int) {
	n, revCnt := len(A), 0
	for i, v := range A {
		if i >= K && A[i-K] > 1 {
			revCnt ^= 1
			A[i-K] -= 2
		}
		if v == revCnt {
			if i+K > n {
				return -1
			}
			ans++
			revCnt ^= 1
			A[i] += 2
		}
	}
	return
}
