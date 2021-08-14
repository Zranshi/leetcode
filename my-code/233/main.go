package main

import "fmt"

// @Time     : 2021/08/13 10:02
// @Author   : Ranshi
// @File     : main.go

func maxInts(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func minInts(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func countDigitOne(n int) (ans int) {
	for k, mulk := 0, 1; n >= mulk; k++ {
		ans += (n/(mulk*10))*mulk + minInts(maxInts(n%(mulk*10)-mulk+1, 0), mulk)
		mulk *= 10
	}
	return
}

func main() {
	fmt.Println(countDigitOne(123456789))
}
