package main

import "fmt"

// @Time     : 2021/7/16 21:36
// @Author   : Ranshi
// @File     : main.go
func printBin(num float64) string {
	res := []rune{'0', '.'}
	for num != float64(0) {
		num *= 2
		if num >= 1 {
			res = append(res, '1')
			num -= 1.0
		} else {
			res = append(res, '0')
		}
		if len(res) > 32 {
			return "ERROR"
		}
	}
	return string(res)
}

func main() {
	fmt.Println(printBin(0.078125))
}
