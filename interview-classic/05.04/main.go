package main

import "fmt"

// @Time     : 2021/7/17 19:53
// @Author   : Ranshi
// @File     : main.go

func findClosedNumbers(num int) []int {
	ans := []int{-1, -1}
	sn, on, find := 0, uint(0), 0
	for num > 0 {
		pn := num & (-num)
		num &= num - 1
		if pn&(1<<30) == 0 && num&(pn<<1) == 0 && ans[0] == -1 {
			ans[0] = num | (pn << 1) | (1<<on - 1)
			find++
		}
		if pn > 1 && sn&(pn>>1) == 0 && ans[1] == -1 {
			ans[1] = num | (pn >> 1) | ((pn>>1 - 1) ^ (pn>>1-1)>>on)
			find++
		}
		if find == 2 {
			break
		}
		sn |= pn
		on++
	}
	return ans
}

func main() {
	fmt.Println(findClosedNumbers(22))
}
