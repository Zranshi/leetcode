package main

// @Time     : 2022/09/16 18:33
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 剑指 Offer II 042. 最近请求次数

type RecentCounter struct {
	que []int
}

func Constructor() RecentCounter {
	return RecentCounter{que: []int{}}
}

func (rc *RecentCounter) Ping(t int) (ans int) {
	rc.que = append(rc.que, t)
	for i := 0; i < len(rc.que); i++ {
		if t-rc.que[i] <= 3000 {
			rc.que = rc.que[i:]
			break
		}
	}
	return len(rc.que)
}
