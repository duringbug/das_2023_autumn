import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np


def two(arr):
    n = len(arr)

    # 创建一个初始状态的图
    fig, ax = plt.subplots()
    ax.bar(range(len(arr)), arr, color='lightblue')
    current_index = 1

    def update(frame):
        nonlocal current_index
        if current_index < n:
            key = arr[current_index]
            j = current_index - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
            ax.clear()
            ax.bar(range(len(arr)), arr, color='lightblue')
            ax.bar(current_index, arr[current_index],
                   color='red', label='Current')
            ax.bar(j, arr[j], color='green', label='Compare')
            ax.set_title(f'Current Index: {current_index}')
            ax.set_xlabel('Index')
            ax.set_ylabel('Value')
            current_index += 1

    # 创建动画
    anim = FuncAnimation(fig, update, frames=range(1, n), repeat=False)
    anim.save('lecture04/resources/insertion_sort.gif', writer='pillow', fps=1)
