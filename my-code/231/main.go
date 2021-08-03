package main

// @Time     : 2021/5/30 00:01
// @Author   : Ranshi
// @File     : 231. 2的幂.go
func isPowerOfTwo(n int) bool {
	for n&1 != 1 && n != 0 {
		n >>= 1
	}
	return n == 1
}
