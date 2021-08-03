package main

func clumsy(N int) (res int) {
	idx, stack := 0, []int{N}
	for i := N - 1; i >= 1; i-- {
		if idx%4 == 0 {
			stack[len(stack)-1] *= i
		} else if idx%4 == 1 {
			stack[len(stack)-1] /= i
		} else if idx%4 == 2 {
			stack = append(stack, i)
		} else {
			stack = append(stack, -1*i)
		}
		idx++
	}
	for _, x := range stack {
		res += x
	}
	return res
}
