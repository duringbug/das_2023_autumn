'''
Description: 
Author: 唐健峰
Date: 2023-09-12 19:32:06
LastEditors: ${author}
LastEditTime: 2023-09-12 19:36:28
'''


a = 1


def Thirteen(n):
    if n < 0:
        print("error input")
        return
    global a
    if n == 0:
        print(a)
        return
    else:
        a = a*n
        return Thirteen(n-1)
