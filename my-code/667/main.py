#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/11/14 08:36
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 677. 键值映射
from typing import Dict


class Data(object):
    def __init__(self) -> None:
        self.dict: Dict[Data] = {}
        self.val = 0


class MapSum(object):
    def __init__(self):
        self.data = Data()

    def insert(self, key: str, val: int) -> None:
        idx = self.data
        for ch in key:
            if ch not in idx.dict:
                idx.dict[ch] = Data()
            idx = idx.dict[ch]
        idx.val = val

    def sum(self, prefix: str) -> int:
        idx = self.data
        for ch in prefix:
            if ch not in idx.dict:
                return 0
            idx = idx.dict[ch]

        def dfs(idx: Data) -> int:
            if idx is None:
                return 0
            return sum(dfs(item) + item.val for item in idx.dict.values())

        return dfs(idx) + idx.val


if __name__ == "__main__":
    ms = MapSum()
    ms.insert("apple", 3)
    print(ms.sum("apple"))
    ms.insert("app", 2)
    print(ms.sum("ap"))
