package main

import "math"

// @Time     : 2021/6/3 22:31
// @Author   : Ranshi
// @File     : 405. 数字转换为十六进制数.go
func toHex(num int) string {
	if num < 0 {
		num += math.MaxUint32 + 1
	}
	if num == 0 {
		return "0"
	}
	var res []int32
	hex := []int32{'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'}
	for num != 0 {
		temp := num % 16
		num = num / 16
		res = append([]int32{hex[temp]}, res...)
	}
	return string(res)
}
