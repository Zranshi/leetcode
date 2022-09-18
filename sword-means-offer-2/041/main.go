package main

// @Time     : 2022/09/16 18:03
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 剑指 Offer II 041. 滑动窗口的平均值
type MovingAverage struct {
	size int
	que  []int
	len  int
	sum  int
}

func Constructor(size int) MovingAverage {
	return MovingAverage{size: size}
}

func (ma *MovingAverage) Next(val int) float64 {
	if ma.len == ma.size {
		ma.sum -= ma.que[0]
		ma.que = ma.que[1:]
	} else {
		ma.len++
	}
	ma.que = append(ma.que, val)
	ma.sum += val
	return float64(ma.sum) / float64(ma.len)
}
