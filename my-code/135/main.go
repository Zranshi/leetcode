package main

import "fmt"

func candy(ratings []int) (ans int) {
	n := len(ratings)
	left := make([]int, n)
	for i, v := range ratings {
		if i > 0 && v > ratings[i-1] {
			left[i] = left[i-1] + 1
		} else {
			left[i] = 1
		}
	}
	right := 0
	for i := n - 1; i >= 0; i-- {
		if i < n-1 && ratings[i] > ratings[i+1] {
			right++
		} else {
			right = 1
		}
		ans += max(left[i], right)
	}
	return
}

func main() {
	fmt.Println(candy([]int{1, 0, 2}))
}
