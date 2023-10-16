'''
Description:
Author: 唐健峰
Date: 2023-10-16 17:58:32
LastEditors: ${author}
LastEditTime: 2023-10-16 18:02:32
'''


def one(num):
    if num <= 1:
        return False
    if num <= 3:
        return True

    if num % 2 == 0 or num % 3 == 0:
        return False

    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6

    return True
