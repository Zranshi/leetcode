package main

import "fmt"

// @Time     : 2021/7/22 21:35
// @Author   : Ranshi
// @File     : main.go

func fib(n int) int {
	if n == 0 {
		return 0
	} else if n < 2 {
		return 1
	}
	a, b := 1, 0
	for i := 2; i <= n; i++ {
		a, b = a+b, a
	}
	return a
}

func main() {
	fmt.Println(fib(4))
}
