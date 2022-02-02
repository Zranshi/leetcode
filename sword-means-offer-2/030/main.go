package main

import "math/rand"

// @Time     : 2022/01/23 19:09
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 剑指 Offer II 030. 插入、删除和随机访问都是 O(1) 的容器

type RandomizedSet struct {
	dict map[int]int
	list []int
}

func Constructor() RandomizedSet {
	dict := make(map[int]int)
	var list []int
	return RandomizedSet{dict, list}
}

func (rs *RandomizedSet) Insert(val int) bool {
	if _, has := rs.dict[val]; has {
		return false
	}
	rs.dict[val] = len(rs.list)
	rs.list = append(rs.list, val)
	return true
}

func (rs *RandomizedSet) Remove(val int) bool {
	if idx, ok := rs.dict[val]; !ok {
		return false
	} else {
		lastIdx := len(rs.list) - 1
		lastVal := rs.list[lastIdx]
		rs.list[idx] = rs.list[lastIdx]
		rs.dict[lastVal] = idx
		rs.list = rs.list[:lastIdx]
		delete(rs.dict, val)
		return true
	}
}

func (rs *RandomizedSet) GetRandom() int {
	return rs.list[rand.Intn(len(rs.list))]
}
