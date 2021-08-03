# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 22
# @Author   : Ranshi
# @File     : 1736. 替换隐藏数字得到的最晚时间.py
class Solution:
    def maximumTime(self, time: str) -> str:
        length = len(time)
        res = time[:]
        for i in range(length):
            if time[i] == '?':
                if i == 0:
                    if res[1] == '?' or res[1] < '4':
                        res = "2" + res[1:]
                    else:
                        res = "1" + res[1:]
                elif i == 1:
                    if res[0] == '2':
                        res = res[:1] + '3' + res[2:]
                    else:
                        res = res[:1] + '9' + res[2:]
                elif i == 3:
                    res = res[:3] + '5' + res[-1:]
                elif i == 4:
                    res = res[:-1] + '9'
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.maximumTime(time="??:??"))
