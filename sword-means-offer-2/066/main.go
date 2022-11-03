package main

import "fmt"

// @Time     : 2022/10/22 17:46
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 剑指 Offer II 066. 单词之和

type Node struct{
    Val int
    Next map[rune]*Node
}

type MapSum struct {
    root *Node
}

func Constructor() MapSum {
    return MapSum{&Node{Val: 0, Next: map[rune]*Node{}}}
}

func (ms *MapSum) Insert(key string, val int) {
    idx := ms.root
    for _, v := range key {
        if _, ok := idx.Next[v]; !ok{
            idx.Next[v] = &Node{Val: 0, Next: map[rune]*Node{}}
        }
        idx = idx.Next[v]
    }
    idx.Val = val
}

func (ms *MapSum) Sum(prefix string) (ans int) {
    idx := ms.root
    for _, v := range prefix {
        if _, ok:= idx.Next[v]; !ok{
            return 0
        }
        idx = idx.Next[v]
    }
    stk := []*Node{idx}
    for len(stk)!=0{
        idx = stk[0]
        ans += idx.Val
        for _, v := range idx.Next {
            stk = append(stk, v)
        }
        stk = stk[1:]
    }
    return
}


func main() {
    ms := Constructor()
    ms.Insert("apple", 3)
    ms.root.Val = 1
    fmt.Println(ms.root.Val)
}
