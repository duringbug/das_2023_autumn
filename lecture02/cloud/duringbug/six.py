'''
Description: 
Author: 唐健峰
Date: 2023-09-25 20:13:57
LastEditors: ${author}
LastEditTime: 2023-09-25 20:25:16
'''


def six(A, B, C, c):
    x_0 = c
    while True:
        x_0 = x_0-f(A, B, C, x_0)/df(A, B, C, x_0)
        if abs(f(A, B, C, x_0)) <= 1.0e-7:
            break
    return x_0


def f(A, B, C, x_0):
    return A*x_0**2+B*x_0+C


def df(A, B, C, x_0):
    return 2*A*x_0+B
