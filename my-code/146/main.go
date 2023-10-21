package main

type Node struct {
	Key   int
	Value int
	Next  *Node
	Prev  *Node
}

type LRUCache struct {
	Head     *Node
	Tail     *Node
	Length   int
	Capacity int
	Mapping  map[int]*Node
}

func Constructor(capacity int) LRUCache {
	node := &Node{}
	return LRUCache{
		Head:     node,
		Tail:     node,
		Length:   0,
		Capacity: capacity,
		Mapping:  make(map[int]*Node, capacity),
	}
}

func (lc *LRUCache) Get(key int) int {
	if node, is := lc.Mapping[key]; is {
		lc.Put(key, node.Value)
		return node.Value
	}
	return -1
}

func (lc *LRUCache) DeleteNode(node *Node) {
	if node == lc.Tail {
		lc.Tail = lc.Tail.Prev
	} else {
		node.Next.Prev = node.Prev
	}
	node.Prev.Next = node.Next

	delete(lc.Mapping, node.Key)

	lc.Length--
}

func (lc *LRUCache) AddNode(node *Node) {
	node.Prev = lc.Head
	node.Next = lc.Head.Next
	if lc.Head.Next != nil {
        lc.Head.Next.Prev = node
	}
	lc.Head.Next = node
	if lc.Tail == lc.Head {
		lc.Tail = lc.Head.Next
	}

	lc.Mapping[node.Key] = node

	lc.Length++
}

func (lc *LRUCache) Put(key int, value int) {
	if node, is := lc.Mapping[key]; is {
		lc.DeleteNode(node)
	}
	if lc.Length == lc.Capacity {
		lc.DeleteNode(lc.Tail)
	}
	node := Node{Value: value, Key: key, Prev: lc.Head, Next: lc.Head.Next}
	lc.AddNode(&node)
}
