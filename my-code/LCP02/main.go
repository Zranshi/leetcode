package main

// @Time     : 2021/6/3 21:30
// @Author   : Ranshi
// @File     : LCP 02. 分式化简.go

func gcdInt(x, y int) int {
	if y == 0 {
		return x
	}
	return gcdInt(y, x%y)
}

func fraction(cont []int) []int {
	a, b := 1, cont[len(cont)-1]
	for i := len(cont) - 2; i >= 0; i-- {
		a += cont[i] * b
		gcd := gcdInt(a, b)
		a, b = b/gcd, a/gcd
	}
	return []int{b, a}
}
