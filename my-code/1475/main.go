package main

import "fmt"

// @Time     : 2022/09/01 00:07
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 1475. 商品折扣后的最终价格

func finalPrices(prices []int) []int {
	n := len(prices)
	ans := make([]int, n)
	st := []int{0}
	for i := n - 1; i >= 0; i-- {
		p := prices[i]
		for len(st) > 1 && st[len(st)-1] > p {
			st = st[:len(st)-1]
		}
		ans[i] = p - st[len(st)-1]
		st = append(st, p)
	}
	return ans
}

func main() {
	fmt.Println(finalPrices([]int{8, 4, 6, 2, 3}))
}
