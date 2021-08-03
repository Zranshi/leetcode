package main

import "fmt"

// @Time     : 2021/7/19 13:56
// @Author   : Ranshi
// @File     : main.go

func convertInteger(A int, B int) (res int) {
	temp := int32(A ^ B)
	for temp != 0 {
		res++
		temp = temp & (temp - 1)
	}
	return
}

func main() {
	fmt.Println(convertInteger(29, 15))
}
