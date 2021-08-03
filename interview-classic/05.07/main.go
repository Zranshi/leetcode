package main

import "fmt"

// @Time     : 2021/7/19 14:00
// @Author   : Ranshi
// @File     : main.go

func exchangeBits(num int) int {
	return (num&0xaaaaaaaa)>>1 | (num&0x55555555)<<1
}

func main() {
	fmt.Println(exchangeBits(2))
}
