package main

func MaxInt(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func maxTurbulenceSize(arr []int) int {
	left, right, length, res := 0, 0, len(arr), 1
	for right < length-1 {
		if left == right {
			if arr[left] == arr[left+1] {
				left++
			}
			right++
		} else {
			if arr[right-1] < arr[right] && arr[right] > arr[right+1] {
				right++
			} else if arr[right-1] > arr[right] && arr[right] < arr[right+1] {
				right++
			} else {
				left = right
			}
		}
		res = MaxInt(res, right-left+1)
	}
	return res
}
