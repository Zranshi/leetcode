package main

func getDiff(x uint8, y uint8) int {
	if x > y {
		return int(x - y)
	}
	return int(y - x)
}

func MaxInt(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func equalSubstring(s string, t string, maxCost int) int {
	length := len(s)
	difference := []int{}
	for i := range s {
		difference = append(difference, getDiff(s[i], t[i]))
	}
	left, right, cost, maxLength := 0, 0, 0, 0
	for right < length {
		cost += difference[right]
		for cost > maxCost {
			cost -= difference[left]
			left++
		}
		maxLength = MaxInt(maxLength, right-left+1)
		right++
	}
	return maxLength
}
