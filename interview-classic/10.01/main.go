package main

import "fmt"

// @Time     : 2021/10/29 22:42
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 面试题 10.01. 合并排序的数组

func merge(A []int, m int, B []int, n int) {
	for p1, p2, tail := m-1, n-1, m+n-1; p1 >= 0 || p2 >= 0; tail-- {
		var cur int
		if p1 == -1 {
			cur = B[p2]
			p2--
		} else if p2 == -1 {
			cur = A[p1]
			p1--
		} else if A[p1] > B[p2] {
			cur = A[p1]
			p1--
		} else {
			cur = B[p2]
			p2--
		}
		A[tail] = cur
	}
}

func main() {
	a := []int{1, 2, 3, 0, 0, 0}
	merge(a, 3, []int{2, 5, 6}, 3)
	fmt.Println(a)
}
