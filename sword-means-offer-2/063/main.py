# -*- coding: UTF-8 -*-
# @Time     : 2022/10/15 22:46
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 剑指 Offer II 063. 替换单词
class Node:
    def __init__(self) -> None:
        self.word = False
        self.d = {}


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.d:
                node.d[ch] = Node()
            node = node.d[ch]
        node.word = True

    def search_root(self, word: str) -> str:
        node = self.root
        res = []
        for ch in word:
            if ch not in node.d:
                return ""
            node = node.d[ch]
            res.append(ch)
            if node.word:
                return "".join(res)

        return ""


class Solution:
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
        words = sentence.split(" ")
        for i, word in enumerate(words):
            root = trie.search_root(word)
            if root != "":
                words[i] = root
        return " ".join(words)


print(
    Solution().replaceWords(
        dictionary=["a", "aa", "aaa", "aaaa"],
        sentence="a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa",
    )
)
