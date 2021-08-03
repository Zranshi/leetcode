package main

// @Time     : 2021/5/30 10:04
// @Author   : Ranshi
// @File     : 225. 用队列实现栈.go

type MyStack struct {
	mainQueue   []int
	assistQueue []int
}

// Constructor /** Initialize your data structure here. */
func Constructor() MyStack {
	return MyStack{}
}

// Push /** Push element x onto stack. */
func (s *MyStack) Push(x int) {
	s.assistQueue = append(s.assistQueue, x)
	for len(s.mainQueue) != 0 {
		s.assistQueue = append(s.assistQueue, s.mainQueue[0])
		s.mainQueue = s.mainQueue[1:]
	}
	s.mainQueue, s.assistQueue = s.assistQueue, s.mainQueue
}

// Pop /** Removes the element on top of the stack and returns that element. */
func (s *MyStack) Pop() (ans int) {
	ans = s.mainQueue[0]
	s.mainQueue = s.mainQueue[1:]
	return
}

// Top /** Get the top element. */
func (s *MyStack) Top() int {
	return s.mainQueue[0]
}

// Empty /** Returns whether the stack is empty. */
func (s *MyStack) Empty() bool {
	return len(s.mainQueue) == 0
}
