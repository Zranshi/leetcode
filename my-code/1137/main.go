package main

import "fmt"

// @Time     : 2021/7/22 21:38
// @Author   : Ranshi
// @File     : main.go

func tribonacci(n int) int {
	if n == 0 {
		return 0
	} else if n <= 2 {
		return 1
	}
	t0, t1, t2 := 0, 1, 1
	for i := 3; i <= n; i++ {
		t0, t1, t2 = t1, t2, t0+t1+t2
	}
	return t2
}

func main() {
	fmt.Println(tribonacci(4))
}
