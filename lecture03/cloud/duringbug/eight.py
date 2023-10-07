'''
Description: 
Author: 唐健峰
Date: 2023-10-07 16:47:39
LastEditors: ${author}
LastEditTime: 2023-10-07 16:54:36
'''
import random
import time
import copy

# 生成随机数列


def generate_random_array(length):
    return [random.randint(1, 1000) for _ in range(length)]

# 选择排序算法


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# 归并排序算法


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# 桶排序


def bucket_sort(arr):
    # 找到最大值和最小值
    max_val = max(arr)
    min_val = min(arr)

    # 计算桶的数量
    bucket_count = (max_val - min_val) // len(arr) + 1

    # 创建桶并初始化为空列表
    buckets = [[] for _ in range(bucket_count)]

    # 将数据分配到桶中
    for num in arr:
        index = (num - min_val) // len(arr)
        buckets[index].append(num)

    # 对每个桶中的数据进行排序
    for bucket in buckets:
        bucket.sort()

    # 合并排序后的桶
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)

    return sorted_arr


# 测试不同长度的随机数列上的排序算法
lengths = [100, 500, 1000, 5000]
sorting_algorithms = {
    '选择排序': selection_sort,
    '归并排序': merge_sort,
    '桶排序': bucket_sort
}


def eight():
    for length in lengths:
        random_array = generate_random_array(length)

        for algorithm_name, sorting_algorithm in sorting_algorithms.items():
            arr_copy = copy.deepcopy(random_array)  # 防止原始数据被修改
            start_time = time.time()
            sorting_algorithm(arr_copy)
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"{algorithm_name} 在长度为 {length} 的随机数列上的运行时间: {elapsed_time:.6f} 秒")
        print()
    return 0
