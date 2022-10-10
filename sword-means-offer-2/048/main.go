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

type Codec struct {
}

func Constructor() Codec {
	return Codec{}
}

// Serializes a tree to a single string.
func (cc *Codec) serialize(root *TreeNode) string {
	if root == nil {
		return ""
	}
	level := []*TreeNode{root}
	levelVal := []string{}
	for {
		nextLevel := []*TreeNode{}
		flag := false
		tmp := []string{}
		for _, node := range level {
			if node == nil {
				nextLevel = append(nextLevel, nil)
				nextLevel = append(nextLevel, nil)
				tmp = append(tmp, "-")
			} else {
				flag = true
				nextLevel = append(nextLevel, node.Left)
				nextLevel = append(nextLevel, node.Right)
				tmp = append(tmp, strconv.Itoa(node.Val))
			}
		}
		if !flag {
			break
		}
		level = nextLevel
		levelVal = append(levelVal, tmp...)
	}
	return strings.Join(levelVal, " ")
}

// Deserializes your encoded data to tree.
func (cc *Codec) deserialize(data string) *TreeNode {
	if data == "" {
		return nil
	}
	vals := strings.Split(data, " ")
	fmt.Println(vals)
	var genTree func(int) *TreeNode

	genTree = func(i int) *TreeNode {
		fmt.Println(i)
		if i >= len(vals) || vals[i] == "-" {
			return nil
		}
		val, _ := strconv.Atoi(vals[i])
		return &TreeNode{
			Val:   val,
			Left:  genTree(i*2 + 1),
			Right: genTree(i*2 + 2),
		}
	}

	return genTree(0)
}

func main() {
	cc := Constructor()
	cStr := cc.serialize(rs_type.TreeNodeInitBySlice([]int{1, 2, 3, 0, 0, 4, 5}))
	fmt.Println(cStr)
	fmt.Println(cc.deserialize(cStr))
}
