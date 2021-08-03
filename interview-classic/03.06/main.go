package main

import "fmt"

// @Time     : 2021/6/29 16:55
// @Author   : Ranshi
// @File     : main.go

type AnimalShelf struct {
	Animals [][]int
}

func Constructor() AnimalShelf {
	return AnimalShelf{}
}

func (s *AnimalShelf) Enqueue(animal []int) {
	s.Animals = append(s.Animals, animal)
}

func (s *AnimalShelf) DequeueAny() (res []int) {
	if len(s.Animals) != 0 {
		res = s.Animals[0]
		s.Animals = s.Animals[1:]
	} else {
		res = []int{-1, -1}
	}
	return
}

func (s *AnimalShelf) dequeue(flag int) (res []int) {
	length := len(s.Animals)
	for i := range s.Animals {
		if s.Animals[i][1] == flag {
			res = s.Animals[i]
			s.Animals = append(s.Animals[:i], s.Animals[i+1:]...)
			break
		}
	}
	if length == len(s.Animals) {
		res = []int{-1, -1}
	}
	return
}

func (s *AnimalShelf) DequeueDog() (res []int) {
	return s.dequeue(1)
}

func (s *AnimalShelf) DequeueCat() (res []int) {
	return s.dequeue(0)
}

func main() {
	s := []int{1, 2, 3, 4, 5, 56, 6, 7, 778, 8, 4, 64, 56}
	fmt.Println(s)
	s = append(s[:1], s[4:]...)
	fmt.Println(s)
}
