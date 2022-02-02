package main

import "fmt"

// @Time     : 2022/01/31 01:22
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 1342. 将数字变成 0 的操作次数

func numberOfSteps(num int) (ans int) {
	for num != 0 {
		if num&1 == 1 {
			num--
		} else {
			num >>= 1
		}
		ans++
	}
	return
}

func main() {
	fmt.Println(numberOfSteps(14))
}
