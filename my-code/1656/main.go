package main

// @Time     : 2022/08/16 22:05
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 1656. 设计有序流

type OrderedStream struct {
	stream []string
	ptr    int
}

func Constructor(n int) OrderedStream {
	return OrderedStream{stream: make([]string, n), ptr: 1}
}

func (os *OrderedStream) Insert(idKey int, value string) []string {
	os.stream[idKey-1] = value
	pre := os.ptr
	for os.ptr <= len(os.stream) && os.stream[os.ptr-1] != "" {
		os.ptr++
	}
	return os.stream[pre-1 : os.ptr-1]
}

func main() {
	os := Constructor(5)
	os.Insert(3, "ccccc")
	os.Insert(1, "aaaaa")
	os.Insert(2, "bbbbb")
	os.Insert(5, "eeeee")
	os.Insert(4, "ddddd")
}
