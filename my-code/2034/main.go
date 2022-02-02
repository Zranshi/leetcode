package main

import "container/heap"

// @Time     : 2022/01/23 10:26
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 2034. 股票价格波动

type pair struct {
	Pirce, Time int
}

type hp []pair

func (h hp) Len() int {
	return len(h)
}
func (h hp) Less(i, j int) bool {
	return h[i].Pirce < h[j].Pirce
}
func (h hp) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}
func (h *hp) Push(v interface{}) {
	*h = append(*h, v.(pair))
}
func (h *hp) Pop() interface{} {
	a := *h
	v := a[len(a)-1]
	*h = a[:len(a)-1]
	return v
}

type StockPrice struct {
	Max, Min    hp
	Mapping     map[int]int
	CurrentTime int
}

func Constructor() StockPrice {
	return StockPrice{Mapping: map[int]int{}}
}

func (sp *StockPrice) Update(timestamp, price int) {
	heap.Push(&sp.Max, pair{-price, timestamp})
	heap.Push(&sp.Min, pair{price, timestamp})
	sp.Mapping[timestamp] = price
	if timestamp > sp.CurrentTime {
		sp.CurrentTime = timestamp
	}
}

func (sp *StockPrice) Current() int {
	return sp.Mapping[sp.CurrentTime]
}

func (sp *StockPrice) Maximum() int {
	for {
		if p := sp.Max[0]; -p.Pirce == sp.Mapping[p.Time] {
			return -p.Pirce
		}
		heap.Pop(&sp.Max)
	}
}

func (sp *StockPrice) Minimum() int {
	for {
		if p := sp.Min[0]; p.Pirce == sp.Mapping[p.Time] {
			return p.Pirce
		}
		heap.Pop(&sp.Min)
	}
}
