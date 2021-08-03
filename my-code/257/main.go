package main

import "fmt"

// @Time     : 2021/5/30 21:04
// @Author   : Ranshi
// @File     : 257. 二叉树的所有路径.go

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

type path struct {
	idx *TreeNode
	str string
}

func binaryTreePaths(root *TreeNode) (res []string) {
	var paths []*path
	paths = append(paths, &path{
		idx: root,
		str: fmt.Sprintf("%d", root.Val),
	})
	for len(paths) != 0 {
		idxRoot, idxPath := paths[0].idx, paths[0].str
		paths = paths[1:]
		if idxRoot.Left != nil || idxRoot.Right != nil {
			if idxRoot.Left != nil {
				paths = append(paths, &path{
					idx: idxRoot.Left,
					str: fmt.Sprintf("%s->%d", idxPath, idxRoot.Left.Val),
				})
			}
			if idxRoot.Right != nil {
				paths = append(paths, &path{
					idx: idxRoot.Right,
					str: fmt.Sprintf("%s->%d", idxPath, idxRoot.Right.Val),
				})
			}
		} else {
			res = append(res, idxPath)
		}
	}
	return res
}
