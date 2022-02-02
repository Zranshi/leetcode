package main

import "fmt"

// @Time     : 2022/02/03 01:23
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 1414. 和为 K 的最少斐波那契数字数目

func findMinFibonacciNumbers(k int) (ans int) {
	fibs := []int{1, 1}
	for {
		val := fibs[len(fibs)-1] + fibs[len(fibs)-2]
		if val > k {
			break
		}
		fibs = append(fibs, val)
	}
	for i := len(fibs) - 1; i >= 0; i-- {
		if k >= fibs[i] {
			ans++
			k -= fibs[i]
		}
	}
	return
}

func main() {
	fmt.Println(findMinFibonacciNumbers(19))
}
