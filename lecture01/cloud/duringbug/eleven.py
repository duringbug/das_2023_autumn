'''
Description: 
Author: 唐健峰
Date: 2023-09-12 18:57:07
LastEditors: ${author}
LastEditTime: 2023-09-12 18:58:48
'''


def Eleven(str: str):
    for i in range(len(str)):
        if str[i] != " ":
            print(str[i], end="")
    print()
