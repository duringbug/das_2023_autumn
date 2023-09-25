'''
Description: 
Author: 唐健峰
Date: 2023-09-25 20:13:57
LastEditors: ${author}
LastEditTime: 2023-09-25 20:47:47
'''


def seven(A, B, C, D, c):
    x_0 = c
    while True:
        x_0 = x_0-f(A, B, C, D, x_0)/df(A, B, C, D, x_0)
        if abs(f(A, B, C, D, x_0)) <= 1.0e-7:
            break
    return x_0


def f(A, B, C, D, x_0):
    return A*x_0**3+B*x_0**2+C*x_0+D


def df(A, B, C, D, x_0):
    return 3*A*x_0**2+2*B*x_0+C
