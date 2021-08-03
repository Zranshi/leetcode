package main

// @Time     : 2021/6/29 16:24
// @Author   : Ranshi
// @File     : main.go

type SortedStack struct {
	St []int
}

func Constructor() SortedStack {
	return SortedStack{}
}

func (s *SortedStack) Push(val int) {
	var assSt []int
	for len(s.St) != 0 && val > s.Peek() {
		assSt = append(assSt, s.Peek())
		s.Pop()
	}
	s.St = append(s.St, val)
	for len(assSt) != 0 {
		s.St = append(s.St, assSt[len(assSt)-1])
		assSt = assSt[:len(assSt)-1]
	}
}

func (s *SortedStack) Pop() {
	if !s.IsEmpty() {
		s.St = s.St[:len(s.St)-1]
	}
}

func (s *SortedStack) Peek() int {
	if s.IsEmpty() {
		return -1
	}
	return s.St[len(s.St)-1]
}

func (s *SortedStack) IsEmpty() bool {
	return len(s.St) == 0
}
