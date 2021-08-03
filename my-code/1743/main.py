# -*- coding:utf-8 -*-
# @Time     : 2021/7/25 08:43
# @Author   : Ranshi
# @File     : main.py
from typing import List


class Solution:
    def restoreArray(self, adjacent_pairs: List[List[int]]) -> List[int]:
        from collections import defaultdict
        mapping, res, path = defaultdict(list), [], set()
        for item in adjacent_pairs:  # 构建哈希表
            mapping[item[0]].append(item[1])
            mapping[item[1]].append(item[0])
        for item in mapping:  # 找到起始点
            if len(mapping[item]) == 1:
                res.append(item)
                path.add(item)
                break
        while len(res) < len(mapping):  # bfs
            idx = res[-1]
            for x in mapping[idx]:
                idx = x if x not in path else idx
            path.add(idx)
            res.append(idx)
        return res


if __name__ == '__main__':
    print(Solution().restoreArray(adjacent_pairs=[[2, 1], [3, 4], [3, 2]]))
