# -*- coding: UTF-8 -*-
# @Time     : 2021/09/16 07:12
# @Author   : Ranshi
# @File     : 123.py
from typing import List


from collections import defaultdict


class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.word = ""

    def insert(self, word):
        cur = self
        for c in word:
            cur = cur.children[c]
        cur.is_word = True
        cur.word = word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)

        def dfs(now, i1, j1):
            if board[i1][j1] not in now.children:
                return

            ch = board[i1][j1]

            nxt = now.children[ch]
            if nxt.word != "":
                ans.append(nxt.word)
                nxt.word = ""

            if nxt.children:
                board[i1][j1] = "#"
                for i2, j2 in [
                    (i1 + 1, j1),
                    (i1 - 1, j1),
                    (i1, j1 + 1),
                    (i1, j1 - 1),
                ]:
                    if 0 <= i2 < m and 0 <= j2 < n:
                        dfs(nxt, i2, j2)
                board[i1][j1] = ch

            if not nxt.children:
                now.children.pop(ch)

        ans = []
        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                dfs(trie, i, j)

        return ans


if __name__ == "__main__":
    print(
        Solution().findWords(
            board=[
                ["o", "a", "a", "n"],
                ["e", "t", "a", "e"],
                ["i", "h", "k", "r"],
                ["i", "f", "l", "v"],
            ],
            words=["oath", "pea", "eat", "rain"],
        )
    )
