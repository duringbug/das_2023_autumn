'''
Description: 
Author: 唐健峰
Date: 2023-09-26 12:59:35
LastEditors: ${author}
LastEditTime: 2023-10-07 17:01:12
'''
from cloud.duringbug.one import one
from cloud.duringbug.two import two
from cloud.duringbug.three import three
from cloud.duringbug.four import LinkedList
from cloud.duringbug.five import five
from cloud.duringbug.six import six
from cloud.duringbug.seven import seven
from cloud.duringbug.eight import eight
from cloud.duringbug.nine import nine


def main():
    # 第一题
    decimal_number = 2.3124
    binary_representation = one(decimal_number, num_places=10)
    print(f"{decimal_number}的二进制是{binary_representation}")
    # 第二题
    two()

    # 第三题
    id_card_number = "510781200407125650"  # 替换成要验证的身份证号码
    if three(id_card_number):
        print(f"{id_card_number} 是合法的身份证号码")
    else:
        print(f"{id_card_number} 不是合法的身份证号码")

    # 第四题
    my_linked_list = LinkedList()
    my_linked_list.append(1)
    my_linked_list.append(2)
    my_linked_list.append(3)

    print("初始链表:")
    my_linked_list.display()

    my_linked_list.delete(2)
    print("删除节点后的链表:")
    my_linked_list.display()

    my_linked_list.update(1, 10)
    print("修改节点后的链表:")
    my_linked_list.display()

    if my_linked_list.search(3):
        print("链表中包含值 3")
    else:
        print("链表中不包含值 3")

    # 第五题
    five()

    # 第六题
    six(-1)
    six(24)
    six(61)
    six(81)
    six(95)

    # 第七题
    print(seven(102, 12))

    # 第八题
    eight()

    # 第九题
    print(nine([1, 2, 3, 4]))

    return 0


if __name__ == '__main__':
    main()
