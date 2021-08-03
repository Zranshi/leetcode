package main

// @Time     : 2021/6/29 16:09
// @Author   : Ranshi
// @File     : main.go

type MyQueue struct {
	MainSt []int
	AssSt  []int
}

func Constructor() MyQueue {
	return MyQueue{}
}

func (q *MyQueue) Push(x int) {
	q.MainSt = append(q.MainSt, x)
}

func (q *MyQueue) change() {
	for len(q.MainSt) != 0 {
		q.AssSt = append(q.AssSt, q.MainSt[len(q.MainSt)-1])
		q.MainSt = q.MainSt[:len(q.MainSt)-1]
	}
}

func (q *MyQueue) Pop() (res int) {
	if len(q.AssSt) == 0 {
		q.change()
	}
	res = q.AssSt[len(q.AssSt)-1]
	q.AssSt = q.AssSt[:len(q.AssSt)-1]
	return
}

func (q *MyQueue) Peek() int {
	if len(q.AssSt) == 0 {
		q.change()
	}
	return q.AssSt[len(q.AssSt)-1]
}

func (q *MyQueue) Empty() bool {
	return len(q.AssSt) == 0 && len(q.MainSt) == 0
}
