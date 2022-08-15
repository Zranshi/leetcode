package main

// @Time     : 2022/08/15 22:37
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 641. 设计循环双端队列

type node struct {
	prev, next *node
	val        int
}

type MyCircularDeque struct {
	head, tail *node
	cap, size  int
}

func Constructor(k int) MyCircularDeque {
	return MyCircularDeque{cap: k}
}

func (mcd *MyCircularDeque) InsertFront(value int) bool {
	if mcd.IsFull() {
		return false
	}

	node := &node{val: value}
	if mcd.IsEmpty() {
		mcd.head = node
		mcd.tail = node
	} else {
		node.next = mcd.head
		mcd.head.prev = node
		mcd.head = node
	}
	mcd.size++

	return true
}

func (mcd *MyCircularDeque) InsertLast(value int) bool {
	if mcd.IsFull() {
		return false
	}

	node := &node{val: value}
	if mcd.IsEmpty() {
		mcd.head = node
		mcd.tail = node
	} else {
		mcd.tail.next = node
		node.prev = mcd.tail
		mcd.tail = node
	}
	mcd.size++

	return true
}

func (mcd *MyCircularDeque) DeleteFront() bool {
	if mcd.IsEmpty() {
		return false
	}

	mcd.head = mcd.head.next
	if mcd.head != nil {
		mcd.head.prev = nil
	}
	mcd.size--

	return true
}

func (mcd *MyCircularDeque) DeleteLast() bool {
	if mcd.IsEmpty() {
		return false
	}

	mcd.tail = mcd.tail.prev
	if mcd.tail != nil {
		mcd.tail.next = nil
	}
	mcd.size--

	return true
}

func (mcd *MyCircularDeque) GetFront() int {
	if mcd.IsEmpty() {
		return -1
	}
	return mcd.head.val
}

func (mcd *MyCircularDeque) GetRear() int {
	if mcd.IsEmpty() {
		return -1
	}
	return mcd.tail.val
}

func (mcd *MyCircularDeque) IsEmpty() bool {
	return mcd.size == 0
}

func (mcd *MyCircularDeque) IsFull() bool {
	return mcd.size == mcd.cap
}
