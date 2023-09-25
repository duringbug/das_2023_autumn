'''
Description:
Author: 唐健峰
Date: 2023-09-19 18:13:32
LastEditors: ${author}
LastEditTime: 2023-09-25 12:31:05
'''
import math

store = {}
son = []


def find_max(num):
    global store
    global son
    if num in store:
        return store[num]
    else:
        max = num
        num_1 = 0
        num_2 = num
        for i in range(1, math.floor(num/2)+1):
            r = find_max(i)*find_max(num-i)
            if r > max:
                max = r
                num_1 = i
                num_2 = num-i
        store[num] = max
        return max
