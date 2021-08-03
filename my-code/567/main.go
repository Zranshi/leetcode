package main

func check(a []int, b []int) bool {
	for i := range a {
		if a[i] != b[i] {
			return false
		}
	}
	return true
}

func checkInclusion(s1 string, s2 string) bool {
	s1Length, s2Length := len(s1), len(s2)
	if s1Length > s2Length {
		return false
	}
	s2 = s2 + "a"
	target := make([]int, 26)
	index := make([]int, 26)
	for i := 0; i < s1Length; i++ {
		target[s1[i]-'a']++
		index[s2[i]-'a']++
	}
	for idx := 0; idx < s2Length-s1Length+1; idx++ {
		//fmt.Println(index)
		if check(index, target) {
			return true
		}
		index[s2[idx+s1Length]-'a'] += 1
		index[s2[idx]-'a'] -= 1
	}
	return false
}
