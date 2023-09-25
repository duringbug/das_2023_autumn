'''
Description: 
Author: 唐健峰
Date: 2023-09-19 18:12:37
LastEditors: ${author}
LastEditTime: 2023-09-25 13:18:53
'''
from cloud.duringbug.one import *
import sys

sys.setrecursionlimit(10000)


def main():
    try:
        num = 2001
        # 不包括1，2，3，因为1，2，3本身就不用分了
        max_finder = MaxFinder()
        result = max_finder.find_max(num)
        # print("Result:", result)
        # print("Store:", max_finder.store)
        # print("Son:", max_finder.son)
        max_finder.print_result(num)
    except:
        print("error input!!!")
    return 0


if __name__ == '__main__':
    main()
