package main

// @Time     : 2021/10/08 08:08
// @Author   : Ranshi
// @File     : main.go
import (
	"fmt"
	"sort"
	"strings"
)

func minNumber(nums []int) string {
	sort.Slice(nums, func(i, j int) bool {
		return (fmt.Sprintf("%d%d", nums[i], nums[j]) <
			fmt.Sprintf("%d%d", nums[j], nums[i]))
	})
	fmt.Println(nums)
	var res strings.Builder
	for i := range nums {
		res.WriteString(fmt.Sprintf("%d", nums[i]))
	}
	return res.String()
}

func main() {
	fmt.Println(minNumber([]int{3, 30, 34, 5, 9}))
}
