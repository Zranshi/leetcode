package main

import "fmt"

// @Time     : 2022/08/18 10:14
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 1224. 最大相等频率   

func maxEqualFreq(nums []int) (ans int) {
	freq := map[int]int{}
	count := map[int]int{}
	maxFreq := 0
	for i, num := range nums {
		if count[num] > 0 {
			freq[count[num]]--
		}
		count[num]++
		maxFreq = max(maxFreq, count[num])
		freq[count[num]]++
		if maxFreq == 1 ||
			freq[maxFreq]*maxFreq+freq[maxFreq-1]*(maxFreq-1) == i+1 && freq[maxFreq] == 1 ||
			freq[maxFreq]*maxFreq+1 == i+1 && freq[1] == 1 {
			ans = max(ans, i+1)
		}
	}
	return
}

func max(a, b int) int {
	if b > a {
		return b
	}
	return a
}

func main() {
	fmt.Println(maxEqualFreq([]int{2, 2, 1, 1, 5, 3, 3, 5}))
}
