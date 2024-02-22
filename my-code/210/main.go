package main

import "fmt"

type LearnPlan struct {
	learnd []bool
	plan   []int
}

func (p *LearnPlan) isLearnd(c int) bool {
	return p.learnd[c]
}

func (p *LearnPlan) learn(c int) {
	p.learnd[c] = true
	p.plan = append(p.plan, c)
}

func (p LearnPlan) isAllLearned() bool {
	for i := 0; i < len(p.learnd); i++ {
		if !p.learnd[i] {
			return false
		}
	}
	return true
}

func findOrder(numCourses int, prerequisites [][]int) []int {
	p := &LearnPlan{
		learnd: make([]bool, numCourses),
		plan:   []int{},
	}

	lockCourses := make([][]int, numCourses)
	for i := 0; i < numCourses; i++ {
		lockCourses[i] = []int{}
	}
	for _, lock := range prerequisites {
		locked, locker := lock[0], lock[1]
		lockCourses[locked] = append(lockCourses[locked], locker)
	}
	idxCourses := []int{}
	for i := 0; i < numCourses; i++ {
		if len(lockCourses[i]) == 0 {
			idxCourses = append(idxCourses, i)
		}
	}
	for len(idxCourses) != 0 {
		for _, c := range idxCourses {
			p.learn(c)
		}
		nextCourses := []int{}
		for c, lock := range lockCourses {
			if p.isLearnd(c) {
				continue
			}
			flag := true
			for _, need := range lock {
				if !p.isLearnd(need) {
					flag = false
					break
				}
			}
			if flag {
				nextCourses = append(nextCourses, c)
			}
		}
		idxCourses = nextCourses
	}
	if p.isAllLearned() {
		return p.plan
	} else {
		return []int{}
	}
}

func main() {
	fmt.Println(findOrder(4, [][]int{
		{1, 0},
		{2, 0},
		{3, 1},
		{3, 2},
	}))
}
