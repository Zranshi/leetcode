package main

import "fmt"

// @Time     : 2021/7/22 20:58
// @Author   : Ranshi
// @File     : main.go

func swapNumbers(numbers []int) []int {
	return []int{numbers[1], numbers[0]}
}

func main() {
	fmt.Println(swapNumbers([]int{1, 2}))
}
