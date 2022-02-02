package main

import "container/list"

// @Time     : 2022/01/24 15:08
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 剑指 Offer II 031. 最近最少使用缓存

type LRUCache struct {
	capacity int
	l        *list.List
	cache    map[int]*list.Element
}

type entry struct {
	key   int
	value int
}

func Constructor(capacity int) LRUCache {
	return LRUCache{
		capacity: capacity,
		l:        list.New(),
		cache:    make(map[int]*list.Element),
	}
}

func (lru *LRUCache) Get(key int) int {
	if ele, ok := lru.cache[key]; ok {
		lru.l.MoveToFront(ele)
		kv := ele.Value.(*entry)
		return kv.value
	}
	return -1
}

func (lru *LRUCache) Put(key int, value int) {
	if ele, ok := lru.cache[key]; ok {
		lru.l.MoveToFront(ele)
		kv := ele.Value.(*entry)
		kv.value = value
	} else {
		ele := lru.l.PushFront(&entry{key, value})
		lru.cache[key] = ele
	}

	if lru.capacity < len(lru.cache) {
		ele := lru.l.Back()
		if ele != nil {
			lru.l.Remove(ele)
			kv := ele.Value.(*entry)
			delete(lru.cache, kv.key)
		}
	}
}
