package main

import "fmt"

// @Time     : 2021/11/19 08:42
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 397. 整数替换

func integerReplacement(n int) (ans int) {
	for n != 1 {
		switch {
		case n%2 == 0:
			ans++
			n /= 2
		case n%4 == 1:
			ans += 2
			n /= 2
		case n == 3:
			ans += 2
			n = 1
		default:
			ans += 2
			n = n/2 + 1
		}
	}
	return
}

func main() {
	fmt.Println(integerReplacement(8))
}
