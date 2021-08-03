package main

// @Time     : 2021/5/30 08:15
// @Author   : Ranshi
// @File     : 202. 快乐数.go

// 哈希表法
func _isHappy(n int) bool {
	numMap := make(map[int]bool)
	var next int
	for n != 1 {
		if _, ok := numMap[n]; ok {
			return false
		}
		numMap[n] = true
		next = 0
		for n != 0 {
			next += (n % 10) * (n % 10)
			n /= 10
		}
		n = next
	}
	return true
}

// 快慢指针法, 速度可能慢一点点，但是内存消耗小呀
func isHappy(n int) bool {
	getNext := func(n int) (ans int) {
		for n != 0 {
			ans += (n % 10) * (n % 10)
			n /= 10
		}
		return
	}
	slow, quick := n, getNext(n)
	for slow != 1 {
		if slow == quick {
			return false
		}
		slow = getNext(slow)
		quick = getNext(getNext(quick))
	}
	return slow == 1
}
