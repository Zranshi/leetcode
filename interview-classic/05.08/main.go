package main

import "fmt"

// @Time     : 2021/7/19 14:13
// @Author   : Ranshi
// @File     : main.go

func drawLine(length int, w int, x1 int, x2 int, y int) []int {
	ret := make([]int, length)
	for i := range ret {
		var idx int32

		for k := 0 + i*32; k < 32+i*32; k++ {
			if k >= x1+y*w && k <= x2+y*w {
				idx |= 1 << (31 - uint(k-i*32))
			}
		}
		ret[i] = int(idx)
	}
	return ret
}

func main() {
	fmt.Println(drawLine(2, 32, 30, 31, 1))
}
