package main

import "fmt"

func hasPath(gene1, gene2 string) bool {
	diffCount := 0
	for i := 0; i < 8; i++ {
		if gene1[i] != gene2[i] {
			diffCount++
		}
		if diffCount > 1 {
			return false
		}
	}
	return diffCount == 1
}

func minMutation(startGene string, endGene string, bank []string) int {
	mark := make(map[string]int, len(bank)+1)
	mark[startGene] = 0
	queue := []string{startGene}
	for len(queue) != 0 {
		idxGene := queue[0]
		for _, gene := range bank {
			if _, exist := mark[gene]; exist {
				continue
			}
			if hasPath(idxGene, gene) {
				if gene == endGene {
					return mark[idxGene] + 1
				}
				mark[gene] = mark[idxGene] + 1
				queue = append(queue, gene)
			}
		}
		queue = queue[1:]
	}
	return -1
}

func main() {
	fmt.Println(minMutation("AACCGGTT", "AACCGGTA", []string{"AACCGGTA", "AACCGCTA", "AAACGGTA"}))
}
