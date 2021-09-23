# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 18: 22
# @Author   : Ranshi
# @File     : 1832. 判断句子是否为全字母句.py
from collections import Counter


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s = "thequickbrownfoxjumpsoverthelazydog"
        c = Counter(s)
        for item in c:
            c[item] = 0
        for item in sentence:
            c[item] += 1

        for item in c:
            if c[item] == 0:
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    print(
        s.checkIfPangram(
            sentence="""uwzvsjguyglmikzwnqajbwkvgyxwbwljydeikgegcxigf
        dtvdbynglclgiyczpuoffemyoihxlkqohkhnkhwzgzfqodvioslmbigeiho
        ehlmanvuchzqjjwgbjtulvhkduhovwakbpvuwhuvmulcyfggnzybuqgbyaqufbzidptgdyuol
        qdjcvgsybaqayofaxvgndbkqnsttstsxyunbnmaidaemttvezqaplpoexpilhgwxqbfhnsjnzdollowjsw
        cxywajhawemnstuogzptessnqndastcsehtgtzhjethsbwvmxucjnegmxokffimduwjpsaocfns
        xvhqfksbiwmmabvobgjwozjylemnucebflymsuuilcipuzawmjlaaluphthkumlujkcmlawtoepyfujikt
        wggyfxhnlcxkzivgjnfewmbxmsspkpijpezkpnfbfwfxftkuuifhmvtlvbluhwcmhgywyfpljlawitl
        gdgtb"""
        )
    )
