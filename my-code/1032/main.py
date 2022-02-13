# -*- coding: UTF-8 -*-
# @Time     : 2021/09/10 17:36
# @Author   : Ranshi
# @File     : 123.py
from typing import List


class StreamChecker:
    def __init__(self, words: List[str]):
        self.root = {}
        self.s = ""
        for word in words:  # 将单词反向插入
            self.insert(word[::-1])

    def insert(self, word):  # 插入一个单词
        r = self.root
        for s in word:
            if s not in r:
                r[s] = {}
            r = r[s]
        r["#"] = 1

    def search(self, word, r):  # 查询某一个字母是否在当前节点的子节点中
        for s in word:
            if s not in r:  # 不存在返回Fasle
                return False, None
            r = r[s]
        if "#" not in r:  # 没有到根节点,记录当前r,避免下次从头访问
            return False, r
        return True, None  # 返回一个合法结果

    def query(self, letter: str) -> bool:
        self.s += letter  # 将每次的字母加入

        r = self.root
        for w in self.s[::-1]:  # 反向查找
            flag, r = self.search(w, r)
            if flag:  # 如果存在,返回True
                return True
            elif r is None:  # 如果当前字母不在子节点中,结束,后续也不可能存在合法的后缀,使得该后缀在数组中.
                return False
        return False


if __name__ == "__main__":
    sc = StreamChecker(["cd", "f", "kl"])
    print(sc.d)
