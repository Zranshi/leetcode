package main

func fairCandySwap(A []int, B []int) []int {
	res := 0
	d := make(map[int]int)
	for _, value := range A {
		res += value
		d[value*2] = value
	}
	for _, value := range B {
		res -= value
	}
	for _, value := range B {
		if val, exist := d[2*value+res]; exist {
			return []int{val, value}
		}
	}
	return []int{-1, -1}
}
