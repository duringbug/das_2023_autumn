'''
Description: 
Author: 唐健峰
Date: 2023-10-16 18:16:39
LastEditors: ${author}
LastEditTime: 2023-10-16 18:31:45
'''


import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np


def four(arr):
    n = len(arr)
    gap = n // 2

    # 创建一个初始状态的图
    fig, ax = plt.subplots()
    ax.bar(range(len(arr)), arr, color='lightblue')
    current_gap = gap

    def update(frame):
        nonlocal gap, current_gap
        if gap >= 1:
            for i in range(current_gap, n):
                temp = arr[i]
                j = i
                while j >= current_gap and arr[j - current_gap] > temp:
                    arr[j] = arr[j - current_gap]
                    j -= current_gap
                    # 绘制当前间隔状态
                    ax.clear()
                    ax.bar(range(len(arr)), arr, color='lightblue')
                    ax.set_title(f'Current Gap: {current_gap}')
                    ax.set_xlabel('Index')
                    ax.set_ylabel('Value')
                arr[j] = temp

            gap //= 2
            current_gap = gap
        else:
            anim.event_source.stop()

    # 创建动画，将fps设置为1以减慢动画
    anim = FuncAnimation(fig, update, frames=range(1, n),
                         repeat=False, interval=1000)
    anim.save('lecture04/resources/shell_sort.gif', writer='pillow', fps=1)
