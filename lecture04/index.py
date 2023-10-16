'''
Description: 
Author: 唐健峰
Date: 2023-10-16 17:55:50
LastEditors: ${author}
LastEditTime: 2023-10-16 18:19:15
'''

import time
import timeit
from cloud.duringbug.one import one
from cloud.duringbug.two import two
from cloud.duringbug.four import four


def main():
    # 第一题,第二题
    start_time = time.time()
    one(13)
    end_time = time.time()
    execution_time = end_time - start_time

    print(f"程序执行时间为：{execution_time} 秒")

    execution_time = timeit.timeit(lambda: one(13), number=1)
    print(f"程序执行时间为：{execution_time} 秒")
    # 第三题
    # 测试
    arr = [12, 11, 10, 5, 6, 2, 32, 43, 104, 213, 21, 47, 23, 65, 32,
           65, 8, 32, 234, 97, 23, 65, 23, 65, 24, 57, 87, 264, 97, 23]
    two(arr)
    # 第四题
    arr = [12, 11, 10, 5, 6, 2, 32, 43, 104, 213, 21, 47, 23, 65, 32,
           65, 8, 32, 234, 97, 23, 65, 23, 65, 24, 57, 87, 264, 97, 23]
    four(arr)
    return 0


if __name__ == '__main__':
    main()
