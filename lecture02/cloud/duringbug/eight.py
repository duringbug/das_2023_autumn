'''
Description: 
Author: 唐健峰
Date: 2023-09-25 20:52:35
LastEditors: ${author}
LastEditTime: 2023-09-25 21:05:06
'''
import random
import math


def eight_first(num_samples):
    inside_circle = 0
    total_samples = num_samples

    for _ in range(num_samples):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        # 计算点到圆心的距离
        distance = x**2 + y**2

        # 如果距离小于1，点在圆内
        if distance <= 1:
            inside_circle += 1

    # 计算π的估计值
    pi_estimate = (inside_circle / total_samples) * 4
    return pi_estimate


def eight_second(num_terms):
    pi_estimate = 0
    for k in range(num_terms):
        # 使用莱布尼茨级数公式来计算π
        pi_estimate += ((-1) ** k) / (2 * k + 1)

    pi_estimate *= 4  # 乘以4以得到π的估计值
    return pi_estimate


def eight_third(num_needles, num_trials):
    inside_circle = 0  # 记录针投入圆内的次数

    for _ in range(num_trials):
        x = random.uniform(0, 1)  # 随机生成x坐标
        y = random.uniform(0, 1)  # 随机生成y坐标
        distance = x**2 + y**2  # 计算点到原点的距离

        if distance <= 1:
            inside_circle += 1  # 如果点在圆内，增加计数

    # 使用投针法公式估算π的值
    estimated_pi = (inside_circle / num_trials) * 4
    return estimated_pi
