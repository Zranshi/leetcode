package main

import (
	"fmt"
)

// @Time     : 2021/7/17 18:53
// @Author   : Ranshi
// @File     : main.go

//func reverseBits(num int) (res int) {
//	if num < 0 {
//		num = 1<<32 + num
//	}
//	bNum := make([]bool, 32)
//	idx := 0
//	for num != 0 {
//		bNum[idx] = num%2 == 1
//		idx, num = idx+1, num>>1
//	}
//	le, mark := -1, 0
//	for ri := range bNum {
//		if !bNum[ri] {
//			mark++
//			for mark > 1 {
//				le++
//				if !bNum[le] {
//					mark--
//				}
//			}
//		}
//		if res < ri-le {
//			res = ri - le
//		}
//	}
//	return res
//}

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
