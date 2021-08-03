package main

// @Time     : 2021/6/3 21:27
// @Author   : Ranshi
// @File     : LCP 01. 猜数字.go
func game(guess []int, answer []int) (ans int) {
	for i := 0; i < len(guess); i++ {
		if guess[i] == answer[i] {
			ans++
		}
	}
	return
}
