package main

import "fmt"

// @Time     : 2021/08/07 09:34
// @Author   : Ranshi
// @File     : main.go

func circularArrayLoop(nums []int) bool {
    length := len(nums)
    numPath := make([]bool, length)
    for i := 0; i < length; i++ {
        // 对每个i进行搜索，如果不全为正或不全为负，则将前面所有点记录为-1
        idx := i
        path := map[int]bool{}
        for {
            // 如果被记录在numPath中，说明该点出发后无法形成循环，则退出，并将path中的点更新到numPath中
            if numPath[idx] {
                break
            }
            // 如果被记录的点在path中，说明存在循环，则返回true;如果没被记录，则将其记录为true
            if path[idx] {
                return true
            }
            path[idx] = true
            next := (idx + nums[idx]%length + length) % length
            // 查找下一个结点，如果相乘为负，说明不全为正，或不全为负
            // 如果下一个结点就是当前结点，说明循环长度为1
            if nums[next]*nums[idx] < 0 || idx == next {
                break
            }
            idx = next
        }
        for key := range path {
            numPath[key] = true
        }
    }
    return false
}

func main() {
    fmt.Println(circularArrayLoop([]int{-2, -3, -9}))
}
