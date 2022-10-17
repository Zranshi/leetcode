# -*- coding: UTF-8 -*-
# @Time     : 2022/10/15 21:56
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 剑指 Offer II 062. 实现前缀树
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

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node.d:
                return False
            node = node.d[ch]
        return node.word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch not in node.d:
                return False
            node = node.d[ch]
        return True
