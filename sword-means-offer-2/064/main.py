# -*- coding: UTF-8 -*-
# @Time     : 2022/10/15 23:08
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 剑指 Offer II 064. 神奇的字典
class Trie:
    def __init__(self):
        self.is_finished = False
        self.child = dict()


class MagicDictionary:
    def __init__(self):
        self.root = Trie()

    def buildDict(self, dictionary: list[str]) -> None:
        for word in dictionary:
            cur = self.root
            for ch in word:
                if ch not in cur.child:
                    cur.child[ch] = Trie()
                cur = cur.child[ch]
            cur.is_finished = True

    def search(self, searchWord: str) -> bool:
        def dfs(node: Trie, pos: int, modified: bool) -> bool:
            if pos == len(searchWord):
                return modified and node.is_finished

            ch = searchWord[pos]
            if ch in node.child:
                if dfs(node.child[ch], pos + 1, modified):
                    return True

            if not modified:
                for cnext in node.child:
                    if ch != cnext:
                        if dfs(node.child[cnext], pos + 1, True):
                            return True

            return False

        return dfs(self.root, 0, False)
