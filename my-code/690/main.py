# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 12
# @Author   : Ranshi
# @File     : 690. 员工的重要性.py
from typing import List


class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees: List['Employee'], targetId: int) -> int:
        for item in employees:
            if item.id == targetId:
                return item.importance + sum([self.getImportance(employees, i)
                                              for i in item.subordinates])
