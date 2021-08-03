package main

// @Time     : 2021/5/30 21:25
// @Author   : Ranshi
// @File     : 258. 各位相加.go
func addDigits(num int) int {
	return (num-1)%9 + 1
}
