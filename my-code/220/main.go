package main

import (
	"math"
	"math/rand"
)

type Node struct {
	Ch       [2]*Node
	Priority int
	Val      int
}

func (n *Node) Cmp(b int) int {
	switch {
	case b < n.Val:
		return 0
	case b > n.Val:
		return 1
	default:
		return -1
	}
}

func (n *Node) Rotate(d int) *Node {
	x := n.Ch[d^1]
	n.Ch[d^1] = x.Ch[d]
	x.Ch[d] = n
	return x
}

type Treap struct {
	Root *Node
}

func (t *Treap) _put(o *Node, Val int) *Node {
	if o == nil {
		return &Node{Priority: rand.Int(), Val: Val}
	}
	d := o.Cmp(Val)
	o.Ch[d] = t._put(o.Ch[d], Val)
	if o.Ch[d].Priority > o.Priority {
		o = o.Rotate(d ^ 1)
	}
	return o
}

func (t *Treap) Put(Val int) {
	t.Root = t._put(t.Root, Val)
}

func (t *Treap) _delete(o *Node, Val int) *Node {
	if d := o.Cmp(Val); d >= 0 {
		o.Ch[d] = t._delete(o.Ch[d], Val)
		return o
	} else if o.Ch[1] == nil {
		return o.Ch[0]
	} else if o.Ch[0] == nil {
		return o.Ch[1]
	}
	d := 0
	if o.Ch[0].Priority > o.Ch[1].Priority {
		d = 1
	}
	o = o.Rotate(d)
	o.Ch[d] = t._delete(o.Ch[d], Val)
	return o
}

func (t *Treap) Delete(Val int) {
	t.Root = t._delete(t.Root, Val)
}

func (t *Treap) LowerBound(Val int) (lb *Node) {
	for o := t.Root; o != nil; {
		switch c := o.Cmp(Val); {
		case c == 0:
			lb = o
			o = o.Ch[0]
		case c > 0:
			o = o.Ch[1]
		default:
			return o
		}
	}
	return
}

func containsNearbyAlmostDuplicate(nums []int, k int, t int) bool {
	for i := range nums {
		for j := i + 1; j <= i+k && j < len(nums); j++ {
			if math.Abs(float64(nums[i]-nums[j])) <= float64(t) {
				return true
			}
		}
	}
	return false
}
