package main

// @Time     : 2021/08/03 23:41
// @Author   : Ranshi
// @File     : main.go

import (
	"fmt"
)

func reverseBits(num int) (res int) {
	mark, le, pre := false, -1, 0
	if num < 0 {
		num = 1<<32 + num
	}
	for ri := 0; num != 0; ri, num = ri+1, num>>1 {
		if num%2 != 1 {
			if !mark {
				mark, pre = true, ri
			} else {
				le, pre = pre, ri
			}
		}
		if res < ri-le {
			res = ri - le
		}
	}
	if mark || res == 32 {
		return res
	}
	return res + 1
}

func main() {
	fmt.Println(reverseBits(-1))
}
