def get_digit_count(number):
    number_str = str(number)
    if '.' in number_str:
        number_str = number_str.split('.')[0]
    integer_part_digit_count = len(number_str)
    return integer_part_digit_count


def Twelve(number):
    if (number > 0):
        min = 10 ** ((get_digit_count(number))//3)
        max = min*10
        while abs(((min+max)/2)**3-number) > 0.0001:
            mid = (min+max)/2
            if mid**3 > number:
                max = mid
            elif mid**3 < number:
                min = mid
            else:
                print(mid)
                return
        print(round((min+max)/2, 4))
    elif (number < 0):
        number = -number
        min = 10 ** ((get_digit_count(number))//3)
        max = min*10
        while abs(((min+max)/2)**3-number) > 0.0001:
            mid = (min+max)/2
            if mid**3 > number:
                max = mid
            elif mid**3 < number:
                min = mid
            else:
                print(mid)
                return
        print(-round((min+max)/2, 4))
    else:
        print(0)
