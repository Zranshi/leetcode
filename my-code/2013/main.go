package main

// @Time     : 2021/5/30 08:15
// @Author   : Ranshi
// @File     : 2013. 检测正方形

type DetectSquares map[int]map[int]int

func Constructor() DetectSquares {
	return DetectSquares{}
}

func (s DetectSquares) Add(point []int) {
	x, y := point[0], point[1]
	if s[y] == nil {
		s[y] = map[int]int{}
	}
	s[y][x]++
	return
}

func (s DetectSquares) Count(point []int) (ans int) {
	x, y := point[0], point[1]
	if s[y] == nil {
		return
	}
	yCnt := s[y]
	for col, colCnt := range s {
		if col != y {
			d := col - y
			ans += colCnt[x] * yCnt[x+d] * colCnt[x+d]
			ans += colCnt[x] * yCnt[x-d] * colCnt[x-d]
		}
	}
	return
}
