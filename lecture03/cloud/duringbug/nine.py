'''
Description: 
Author: 唐健峰
Date: 2023-10-07 16:59:46
LastEditors: ${author}
LastEditTime: 2023-10-07 16:59:49
'''


def nine(A):
    n = len(A)

    # 初始化左右两个辅助数组
    left = [1] * n
    right = [1] * n

    # 计算左边乘积
    for i in range(1, n):
        left[i] = left[i - 1] * A[i - 1]

    # 计算右边乘积
    for i in range(n - 2, -1, -1):
        right[i] = right[i + 1] * A[i + 1]

    # 计算 B[i]
    B = [left[i] * right[i] for i in range(n)]

    return B
