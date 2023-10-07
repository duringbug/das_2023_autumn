'''
Description: 
Author: 唐健峰
Date: 2023-10-07 16:37:17
LastEditors: ${author}
LastEditTime: 2023-10-07 16:39:26
'''


def six(score):
    if score < 0 or score > 100:
        print("输入错误")
    elif score < 60:
        print("不及格")
    elif score < 75:
        print("合格")
    elif score < 90:
        print("良好")
    else:
        print("优秀")
    return 0
