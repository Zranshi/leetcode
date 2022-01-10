package main

import "fmt"

// @Time     : 2022/01/09 09:19
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 剑指 Offer II 017. 含有所有字符的最短字符串

func minWindow(s string, t string) string {
	if len(s) < len(t) {
		return ""
	}
	// 标记数组1：字符t出现的次数（0~25：a~z，26~51：A~Z）
	f1 := [52]int{}
	for i := 0; i < len(t); i++ {
		f1[toIndex(t[i])]++
	}
	// 当前窗口的s出现字符次数统计
	total := [52]int{}
	// 标记数组2：当前窗口字符s的相对次数（如果total中某个字符满足题意，置为与f1相同）
	f2 := [52]int{}

	// 根据total窗口结果，设置当前窗口标记f2
	//（某个字符出现次数满足f1，标记为f1的数量，否则为0，主要是为了利用数组“==”快速比较是否满足题意）
	setFlag := func(charIndex int) {
		if total[charIndex] >= f1[charIndex] {
			f2[charIndex] = f1[charIndex]
		} else {
			f2[charIndex] = 0
		}
	}

	// 双指针：记录字符次数total，并设计标记数组f2
	result, rl, rr := 0, -1, -1
	left, right := 0, 0
	for right < len(s) {
		index := toIndex(s[right])
		total[index]++
		setFlag(index)
		if f2 == f1 {
			// 缩小左端：找到第一个不满足的位置
			for f2 == f1 {
				charIndex := toIndex(s[left])
				total[charIndex]--
				setFlag(charIndex)
				left++
			}
			// 有效位置为：left-1 到 right
			temp := right - left + 2
			if result == 0 || temp < result {
				result = temp
				// 有效位[rl, rr]
				rl = left - 1
				rr = right + 1
			}
		}
		right++
	}
	if result == 0 {
		return ""
	}
	return s[rl:rr]
}

// 转数组下标0~25/26~51
func toIndex(c byte) int {
	if c >= 'a' && c <= 'z' {
		return int(c - 'a')
	} else {
		return int(c-'A') + 26
	}
}

func main() {
	fmt.Println(minWindow("XYZXY", "XYZ"))
}
