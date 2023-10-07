'''
Description: 
Author: 唐健峰
Date: 2023-09-12 18:21:51
LastEditors: ${author}
LastEditTime: 2023-09-12 18:31:39
'''


def Four():
    for i in range(3):
        if i == 1:
            for j in range(1):
                print(chr(0x2605), end='')
            print("数据科学与工程导论", end='')
            for j in range(1):
                print(chr(0x2605), end='')
        else:
            for j in range(20):
                print(chr(0x2605), end='')
        print()
