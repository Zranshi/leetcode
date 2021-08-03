# -*- coding:utf-8 -*-
# @Time     : 2021/7/6 08: 22
# @Author   : Ranshi
# @File     : main.py
from typing import List


class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        menu, foods = {}, set()
        for item in orders:
            table_num = int(item[1])
            foods.add(item[2])
            if table_num not in menu:
                menu[table_num] = {}
            if item[2] not in menu[table_num]:
                menu[table_num][item[2]] = 1
            else:
                menu[table_num][item[2]] += 1
        foods, table_l = sorted(list(foods)), sorted(menu.keys())
        res = [['Table'] + foods]
        for key in table_l:
            idx = [str(key)]
            for item in foods:
                if item in menu[key]:
                    idx.append(str(menu[key][item]))
                else:
                    idx.append('0')
            res.append(idx)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.displayTable(
        orders=[["David", "3", "Ceviche"], ["Corina", "10", "Beef Burrito"], ["David", "3", "Fried Chicken"],
                ["Carla", "5", "Water"], ["Carla", "5", "Ceviche"], ["Rous", "3", "Ceviche"]]))
