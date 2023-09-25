'''
Description:
Author: 唐健峰
Date: 2023-09-19 18:13:32
LastEditors: ${author}
LastEditTime: 2023-09-25 13:17:15
'''
import math


class MaxFinder:
    def __init__(self):
        self.store = {}
        self.son = {}

    def find_max(self, num):
        if num in self.store:
            return self.store[num]
        else:
            max_value = num
            num_1 = 0
            num_2 = num
            for i in range(1, math.floor(num/2)+1):
                r = self.find_max(i) * self.find_max(num-i)
                if r > max_value:
                    max_value = r
                    num_1 = i
                    num_2 = num-i
            self.store[num] = max_value
            self.son[num] = [num_1, num_2]
            return max_value

    def print_result(self, num):
        if num <= 3:
            print(num, end=" ")
        else:
            self.print_result(self.son[num][0])
            self.print_result(self.son[num][1])
