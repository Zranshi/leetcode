# -*- coding: UTF-8 -*-
# @Time     : 2021/09/01 07:29
# @Author   : Ranshi
# @File     : main.py


class Solution:

    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(item) for item in version1.split('.')]
        v2 = [int(item) for item in version2.split('.')]
        idx = 0
        while idx < len(v1) or idx < len(v2):
            idx_v1, idx_v2 = 0, 0
            if idx < len(v1):
                idx_v1 = v1[idx]
            if idx < len(v2):
                idx_v2 = v2[idx]
            if idx_v1 != idx_v2:
                return 1 if idx_v1 > idx_v2 else -1
            else:
                idx += 1
        return 0


if __name__ == '__main__':
    print(Solution().compareVersion(version1="1.0.1", version2="1"))
