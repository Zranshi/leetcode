package main

import "fmt"

// @Time     : 2021/7/16 21:17
// @Author   : Ranshi
// @File     : main.go

func insertBits(N int, M int, i int, j int) int {
	var (
		insert func(val, idx int)
	)
	insert = func(val, idx int) {
		if N>>idx&1 != val {
			N ^= 1 << idx
		}
	}
	for iter := i; iter <= j; iter++ {
		ant := 0
		if M != 0 {
			ant = M % 2
			M >>= 1
		}
		insert(ant, iter)
	}
	return N
}

func main() {
	fmt.Println(insertBits(1024, 19, 2, 6))
}
