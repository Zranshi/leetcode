# -*- coding: UTF-8 -*-
# @Time     : 2021/08/25 13:45
# @Author   : Ranshi
# @File     : 123.py

t = int(input())
for _ in range(t):
    usr = input()
    if not usr[0].isalpha() or not usr.isalnum():
        print("Wrong")
    else:
        if not usr.isalpha() and not usr.isdigit():
            print("Accept")
        else:
            print("Wrong")
