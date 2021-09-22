package main

import "fmt"

// @Time     : 2021/09/12 08:13
// @Author   : Ranshi
// @File     : main.go

func findComplement(num int) (ans int) {
	idx := 0
	for num != 0 {
		ans = ans + (num&1^1)<<idx
		num >>= 1
		idx++
	}
	return
}

func main() {
	fmt.Println(findComplement(5))
}
