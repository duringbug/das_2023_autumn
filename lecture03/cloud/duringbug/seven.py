'''
Description: 
Author: 唐健峰
Date: 2023-10-07 16:42:07
LastEditors: ${author}
LastEditTime: 2023-10-07 16:42:16
'''


def seven(a, b):
    while b:
        a, b = b, a % b
    return a
