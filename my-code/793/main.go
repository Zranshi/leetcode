package main

import (
	"fmt"
	"sort"
)

// @Time     : 2022/08/28 12:23
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 793. 阶乘函数后 K 个零

func zeta(n int) (res int) {
	for n > 0 {
		n /= 5
		res += n
	}
	return
}

func nx(k int) int {
	return sort.Search(5*k, func(x int) bool { return zeta(x) >= k })
}

func preimageSizeFZF(k int) int {
	return nx(k+1) - nx(k)
}

func main() {
	fmt.Println(preimageSizeFZF(5))
}
