package main

import "fmt"

// @Time     : 2021/09/26 07:10
// @Author   : Ranshi
// @File     : main.go

func getSum(a int, b int) int {
	for b != 0 {
		carry := uint(a&b) << 1
		a ^= b
		b = int(carry)
	}
	return a
}

func main() {
	fmt.Printf("%v\n", getSum(1, 2))
}
