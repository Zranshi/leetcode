package main

import "fmt"

// @Time     : 2022/11/05 13:03
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 剑指 Offer II 070. 排序数组中只出现一次的数字

func singleNonDuplicate(nums []int) (ans int) {
	for i := 0; i < len(nums); i++ {
        ans ^= nums[i]
    }
    return
}

func main() {
	fmt.Println(singleNonDuplicate([]int{1, 1, 2, 3, 3, 4, 4, 8, 8}))
}
