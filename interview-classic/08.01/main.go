package main

import "fmt"

// @Time     : 2021/7/19 14:27
// @Author   : Ranshi
// @File     : main.go

func waysToStep(n int) int {
	const MOD int = 1000000007
	switch n {
	case 1:
		return 1
	case 2:
		return 2
	}
	a, b, c := 4, 2, 1
	for i := 3; i < n; i++ {
		a, b, c = (a+b+c)%MOD, a, b
	}
	return a
}

func main() {
	fmt.Println(waysToStep(10))
}
