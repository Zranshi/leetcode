package main

type BSTIterator struct {
	queue []int
	idx   int
}

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func (b *BSTIterator) Next() int {
	b.idx += 1
	return b.queue[b.idx-1]
}

func (b *BSTIterator) HasNext() bool {
	return b.idx < len(b.queue)
}

func (b *BSTIterator) InOrder(root *TreeNode) {
	if root.Left != nil {
		b.InOrder(root.Left)
	}
	b.queue = append(b.queue, root.Val)
	if root.Right != nil {
		b.InOrder(root.Right)
	}
}
