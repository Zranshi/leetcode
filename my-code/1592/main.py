# -*- coding: UTF-8 -*-
# @Time     : 2022/09/07 01:32
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 1592. 重新排列单词间的空格


class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = [item for item in text.split(" ") if item != ""]
        space_num = len([ch for ch in text if ch == " "])
        if len(words) == 1:
            return words[0] + " " * space_num
        gap, end_space = divmod(space_num, len(words) - 1)
        return (" " * gap).join(words) + " " * end_space


if __name__ == "__main__":
    print(Solution().reorderSpaces(text="  this   is  a sentence "))
