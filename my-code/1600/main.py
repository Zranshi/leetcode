# -*- coding:utf-8 -*-
# @Time     : 2021/6/22 08: 29
# @Author   : Ranshi
# @File     : 1600. 皇位继承顺序.py
from typing import List


class ThroneInheritance:
    def __init__(self, king_name: str):
        self.idx_king = king_name
        self.root = {king_name: []}
        self.death_set = set()

    def birth(self, parent_name: str, child_name: str) -> None:
        if parent_name in self.root:
            self.root[parent_name].append(child_name)
        else:
            self.root[parent_name] = [child_name]

    def death(self, name: str) -> None:
        self.death_set.add(name)

    def getInheritanceOrder(self) -> List[str]:
        res = [self.idx_king]

        def dfs(father_name: str):
            for name in self.root[father_name]:
                if name not in self.death_set:
                    res.append(name)
                if name in self.root:
                    dfs(name)

        dfs(self.idx_king)
        return res


if __name__ == "__main__":
    t = ThroneInheritance("king")
    t.getInheritanceOrder()
    t.birth("king", "andy")
    t.getInheritanceOrder()
    t.birth("king", "bob")
    t.getInheritanceOrder()
    t.birth("king", "catherine")
    t.getInheritanceOrder()
    t.birth("andy", "matthew")
    t.getInheritanceOrder()
    t.birth("bob", "alex")
    t.getInheritanceOrder()
    t.birth("bob", "asha")
    t.getInheritanceOrder()
    t.death("bob")
    t.getInheritanceOrder()
