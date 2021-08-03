package main

// @Time     : 2021/5/30 08:01
// @Author   : Ranshi
// @File     : 172. 阶乘后的零.go
func trailingZeroes(n int) (ans int) {
	for i := 1; i <= n; i++ {
		cur := i
		for cur%5 == 0 {
			ans++
			cur /= 5
		}
	}
	return
}
