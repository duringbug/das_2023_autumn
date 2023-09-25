'''
Description: 
Author: 唐健峰
Date: 2023-09-19 18:12:37
LastEditors: ${author}
LastEditTime: 2023-09-25 21:17:24
'''
from cloud.duringbug.one import *
from cloud.duringbug.two import two
from cloud.duringbug.three import three
from cloud.duringbug.four import four
from cloud.duringbug.five import five
from cloud.duringbug.six import six
from cloud.duringbug.seven import seven
from cloud.duringbug.eight import *
from cloud.duringbug.nine import nine
import sys

sys.setrecursionlimit(10000)


def main():
    # 第一题
    try:
        num = 2001
        # 不包括1，2，3，因为1，2，3本身就不用分了
        max_finder = MaxFinder()
        result = max_finder.find_max(num)
        # print("Result:", result)
        # print("Store:", max_finder.store)
        # print("Son:", max_finder.son)
        max_finder.print_result(num)
        print()
    except:
        print("error input!!!")
    print()
    # 第二题
    two()
    print()
    # 第三题
    three()
    print()
    # 第四题
    print(four(2))
    print()
    # 第五题
    print(five(1, 0, -2, 2))
    print(five(1, 0, -2, 2000))
    print()
    # 第六题
    print(six(1, 0, -2, 100))
    print(six(1, 0, -2, 50))
    print(six(1, 0, -2, 25))
    print()
    # 第七题
    print(seven(1, 2, 3, 4, 10))
    print()
    # 第八题
    print(f'蒙特卡洛方法:{eight_first(1000000):.10f}')
    print(f'无限级数:{eight_second(1000000):.10f}')
    print(f'投针法{eight_third(1000000,1000000):.10f}')
    print()
    # 第九题
    print(f'{nine(1000000):.10f}')
    return 0


if __name__ == '__main__':
    main()
