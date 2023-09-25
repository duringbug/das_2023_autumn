'''
Description: 
Author: 唐健峰
Date: 2023-09-19 18:12:37
LastEditors: ${author}
LastEditTime: 2023-09-25 12:29:18
'''
from cloud.duringbug.one import find_max
import sys

sys.setrecursionlimit(10000)


def main():
    # 不包括1，2，3，因为1，2，3本身就不用分了
    print(find_max(4))
    return 0


if __name__ == '__main__':
    main()
