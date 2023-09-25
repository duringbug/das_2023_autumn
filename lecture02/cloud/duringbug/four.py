
def four(sqr_num):
    max = sqr_num
    min = 0
    mid = (max+min)/2
    while abs(mid**2-sqr_num) > 1.0e-7:
        if mid**2 > sqr_num:
            max = mid
            mid = (min+mid)/2
        else:
            min = mid
            mid = (max+mid)/2
    return mid
