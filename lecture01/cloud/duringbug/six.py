'''
Description: 
Author: 唐健峰
Date: 2023-09-12 18:36:30
LastEditors: ${author}
LastEditTime: 2023-09-12 18:37:52
'''


def Six(x, y, z, w):
    numbers = [x, y, z, w]
    numbers.sort()
    numbers.reverse()
    for number in numbers:
        print(number, end="\t")
    print()
