package main

import (
	"container/heap"
	"fmt"
	"math"
	"sort"
)

// @Time     : 2022/09/11 11:14
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 857. 雇佣 K 名工人的最低成本

func mincostToHireWorkers(quality, wage []int, k int) float64 {
	n := len(quality)
	h := make([]int, n)
	for i := range h {
		h[i] = i
	}
	sort.Slice(h, func(i, j int) bool {
		a, b := h[i], h[j]
		return quality[a]*wage[b] > quality[b]*wage[a]
	})
	totalq := 0
	q := hp{}
	for i := 0; i < k-1; i++ {
		totalq += quality[h[i]]
		heap.Push(&q, quality[h[i]])
	}
	ans := 1e9
	for i := k - 1; i < n; i++ {
		idx := h[i]
		totalq += quality[idx]
		heap.Push(&q, quality[idx])
		ans = math.Min(ans, float64(wage[idx])/float64(quality[idx])*float64(totalq))
		totalq -= heap.Pop(&q).(int)
	}
	return ans
}

type hp struct{ sort.IntSlice }

func (h hp) Less(i, j int) bool  { return h.IntSlice[i] > h.IntSlice[j] }
func (h *hp) Push(v interface{}) { h.IntSlice = append(h.IntSlice, v.(int)) }
func (h *hp) Pop() interface{} {
	a := h.IntSlice
	v := a[len(a)-1]
	h.IntSlice = a[:len(a)-1]
	return v
}

func main() {
	fmt.Println(mincostToHireWorkers([]int{10, 20, 5}, []int{70, 50, 30}, 2))
}