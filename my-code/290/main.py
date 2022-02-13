# coding: utf-8
# @Time     : 2021/08/11 11:12
# @Author   : Ranshi
# @File     : 123.py


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapping, rev_mapping = {}, {}
        chs_l = s.split(" ")
        if len(chs_l) != len(pattern):
            return False
        for i in range(len(pattern)):
            if chs_l[i] in mapping and pattern[i] in rev_mapping:
                if mapping[chs_l[i]] != pattern[i] or rev_mapping[pattern[i]] != chs_l[i]:
                    return False
            elif chs_l[i] not in mapping and pattern[i] not in rev_mapping:
                mapping[chs_l[i]] = pattern[i]
                rev_mapping[pattern[i]] = chs_l[i]
            else:
                return False
        return True


if __name__ == "__main__":
    print(Solution().wordPattern(pattern="abba", s="dog cat cat dog"))
