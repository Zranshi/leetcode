# -*- coding:utf-8 -*-
# @Time     : 2021/7/5 09: 18
# @Author   : Ranshi
# @File     : main.py


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        from sortedcontainers import SortedDict

        n = len(formula)
        name_cnt_depth = []  # 名字-频率-括号深度
        DEPTH = 0  # 每到一处，左括号的个数就是当前name的深度
        i = 0
        while i < n:
            # --------------------------------（1）找名字
            name = ""
            if formula[i].isupper():  # 大写字母开头
                name += formula[i]
                i += 1
            if name != "":  # 后面跟着小写字母
                while i < n and formula[i].islower():
                    name += formula[i]
                    i += 1
            if name != "":  # 有名字！！！！！！
                # ------------------------------（2）这个名字的次数
                cnt = 0
                # ----如果name后面有数字
                if i < n and formula[i].isdigit():
                    while i < n and formula[i].isdigit():
                        cnt = cnt * 10 + int(formula[i])
                        i += 1
                    name_cnt_depth.append([name, cnt, DEPTH])
                # ----若name后面没数字
                else:
                    name_cnt_depth.append([name, 1, DEPTH])

            # --------------------------------（3）括号的情况
            if i < n and formula[i] == "(":
                DEPTH += 1
                i += 1
            elif i < n and formula[i] == ")":
                i += 1
                cnt = 0
                # ----------后面有数字
                if i < n and formula[i].isdigit():
                    while i < n and formula[i].isdigit():
                        cnt = cnt * 10 + int(formula[i])
                        i += 1
                # ----------后面不是数字
                else:
                    cnt = 1

                # ------------------(4)')'后面的倍数
                for j in range(len(name_cnt_depth) - 1, -1, -1):
                    if name_cnt_depth[j][2] == DEPTH:  # 是当前的深度
                        name_cnt_depth[j][1] *= cnt  # 字母复制
                        name_cnt_depth[j][2] -= 1  # 深度-1
                    else:
                        break
                DEPTH -= 1  # 当前深度的都计算好了,深度可以-1了

        name_freq = SortedDict()
        for name, cnt, depth in name_cnt_depth:
            if name not in name_freq:
                name_freq[name] = 0
            name_freq[name] += cnt

        res = ""
        for name, freq in name_freq.items():
            res += name
            if freq > 1:
                res += str(freq)
        return res
