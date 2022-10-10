package main

import (
	"fmt"
	rs_type "leetcode/type"
	"strconv"
	"strings"
)

// @Time     : 2022/10/07 00:34
// @Author   : Ranshi
// @File     : main.go
// @Doc      : 剑指 Offer II 048. 序列化与反序列化二叉树

type TreeNode = rs_type.TreeNode

type Codec struct{}

func Constructor() (_ Codec) {
	return
}

func (Codec) serialize(root *TreeNode) string {
	sb := &strings.Builder{}
	var dfs func(*TreeNode)
	dfs = func(node *TreeNode) {
		if node == nil {
			sb.WriteString("null,")
			return
		}
		sb.WriteString(strconv.Itoa(node.Val))
		sb.WriteByte(',')
		dfs(node.Left)
		dfs(node.Right)
	}
	dfs(root)
	return sb.String()
}

func (Codec) deserialize(data string) *TreeNode {
	sp := strings.Split(data, ",")
	var build func() *TreeNode
	build = func() *TreeNode {
		if sp[0] == "null" {
			sp = sp[1:]
			return nil
		}
		val, _ := strconv.Atoi(sp[0])
		sp = sp[1:]
		return &TreeNode{Val: val, Left: build(), Right: build()}
	}
	return build()
}

func main() {
	cc := Constructor()
	cStr := cc.serialize(rs_type.TreeNodeInitBySlice([]int{1, 2, 3, 0, 0, 4, 5}))
	fmt.Println(cStr)
	fmt.Println(cc.deserialize(cStr))
}
