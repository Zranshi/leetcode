package main

// @Time     : 2021/5/30 20:53
// @Author   : Ranshi
// @File     : 242. 有效的字母异位词.go
func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}
	diff := make(map[uint8]int)
	for i := 0; i < len(s); i++ {
		if _, ok := diff[s[i]]; ok {
			diff[s[i]]++
		} else {
			diff[s[i]] = 1
		}
		if _, ok := diff[t[i]]; ok {
			diff[t[i]]--
		} else {
			diff[t[i]] = -1
		}
	}
	for _, x := range diff {
		if x != 0 {
			return false
		}
	}
	return true
}
