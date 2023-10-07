'''
Description: 
Author: 唐健峰
Date: 2023-10-07 16:21:53
LastEditors: ${author}
LastEditTime: 2023-10-07 16:25:22
'''
import re


def three(id_card):
    # 正则表达式模式匹配18位身份证号码
    pattern = r'^[1-9]\d{5}(19|20)\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])\d{3}([0-9]|X)$'

    # 使用re模块进行匹配
    if re.match(pattern, id_card):
        return True
    else:
        return False
