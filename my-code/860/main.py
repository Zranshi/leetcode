# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 15
# @Author   : Ranshi
# @File     : 860. Lemonade Change.py
from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if bills[0] != 5:
            return False
        change = [1, 0, 0]  # 分别表示5，10，20元钱的数量
        for i in range(1, len(bills)):
            if bills[i] == 5:
                change[0] += 1
                continue
            elif bills[i] == 10:
                if change[0] != 0:
                    change[0] -= 1
                    change[1] += 1
                    continue
                else:
                    return False
            elif bills[i] == 20:
                if change[0] != 0:
                    if change[1] != 0:
                        change[1] -= 1
                        change[0] -= 1
                        change[2] += 1
                        continue
                    else:
                        if change[0] >= 3:
                            change[0] -= 3
                            change[2] += 1
                            continue
                        else:
                            return False
                else:
                    return False
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.lemonadeChange([5, 5, 5, 10, 20]))
