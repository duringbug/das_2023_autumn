'''
Description: 
Author: 唐健峰
Date: 2023-09-12 18:49:58
LastEditors: ${author}
LastEditTime: 2023-09-12 18:56:22
'''


def Ten(str: str):
    if len(str) == 1:
        print("否")
        return
    else:
        for i in range(len(str)-1):
            if str[i] == str[i+1]:
                print("是")
                return
    print("否")
