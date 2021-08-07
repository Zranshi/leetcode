package main

import "fmt"

// @Time     : 2021/08/07 13:03
// @Author   : Ranshi
// @File     : main.go

func getRow(rowIndex int) []int {
	row := make([]int, rowIndex+1)
	row[0] = 1
	for i := 1; i <= rowIndex; i++ {
		for j := i; j > 0; j-- {
			row[j] += row[j-1]
		}
	}
	return row
}

func main() {
	fmt.Println(getRow(3))
}
