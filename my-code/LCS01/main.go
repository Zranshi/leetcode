package main

import "fmt"

func leastMinutes(n int) int {
	bandwith, res := 1, 1
	for bandwith < n {
		bandwith *= 2
		res++
	}
	return res
}

func main() {
	fmt.Println(leastMinutes(2))
}
