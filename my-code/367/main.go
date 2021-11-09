package main

import "fmt"

// @Time     : 2021/5/31 14:48
// @Author   : Ranshi
// @File     : 367. 有效的完全平方数.go
func isPerfectSquare(num int) bool {
	if num < 2 {
		return true
	}
	min, max := 0, num/2+1
	for max >= min {
		mid := (max-min)/2 + min
		if num > mid*mid {
			min = mid + 1
		} else if num < mid*mid {
			max = mid - 1
		} else {
			return true
		}
	}
	return false
}

func main() {
	fmt.Println(isPerfectSquare(16))
}
