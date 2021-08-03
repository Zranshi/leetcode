package main

type MinStack struct {
	stack    []int
	minStack []int
	length   int
}

func MinInt(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func (s *MinStack) Push(val int) {
	s.stack = append(s.stack, val)
	top := s.GetMin()
	s.minStack = append(s.minStack, MinInt(val, top))
}

func (s *MinStack) Pop() {
	s.minStack = s.minStack[:len(s.minStack)-1]
	s.stack = s.stack[:len(s.stack)-1]
	s.length--
}

func (s *MinStack) Top() int {
	return s.stack[len(s.stack)-1]
}

func (s *MinStack) GetMin() int {
	return s.minStack[len(s.minStack)-1]
}
