'''
Description: 
Author: 唐健峰
Date: 2023-09-25 21:06:49
LastEditors: ${author}
LastEditTime: 2023-09-25 21:18:26
'''
from scipy import integrate
import math
import random


def nine(num_samples):
    count_inside = 0

    for _ in range(num_samples):
        x = random.uniform(2, 3)  # 选择 x 在 [1, 3] 之间随机取值
        y = random.uniform(0, 21)  # 选择 y 在 [0, 21] 之间随机取值

        if y <= f(x):
            count_inside += 1

    estimated_area = (count_inside / num_samples) * 21  # 21 是矩形的面积
    return estimated_area


def f(x):
    return x**2 + 4 * x * math.sin(x)
