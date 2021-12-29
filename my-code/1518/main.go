package main

import "fmt"

// @Time     : 2021/12/17 08:41
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 1518. 换酒问题

func numWaterBottles(numBottles int, numExchange int) int {
	ans := numBottles
	for numBottles >= numExchange {
		ans, numBottles = ans+numBottles/numExchange, numBottles%numExchange+numBottles/numExchange
	}
	return ans
}

func main() {
	fmt.Println(numWaterBottles(9, 3))
}
