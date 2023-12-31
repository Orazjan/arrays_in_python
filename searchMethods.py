import time
import math
import random


def LinearSearch(lys, element):
    for i in range(len(lys)):
        if lys[i] == element:
            return i
    return -1


def BinarySearch(lys, val):
    first = 0
    last = len(lys) - 1
    index = -1

    while first <= last and index == -1:
        mid = (first + last) // 2
        if lys[mid] == val:
            index = mid
        else:
            if val < lys[mid]:
                last = mid - 1
            else:
                first = mid + 1

    return index


def jump_search(lys, val):
    length = len(lys)
    jump = int(math.sqrt(length))
    left, right = 0, 0

    while left < length and lys[left] <= val:
        right = min(length - 1, left + jump)

        if lys[left] <= val and lys[right] >= val:
            break

        left += jump

    if left >= length or lys[left] > val:
        return -1

    right = min(length - 1, right)
    i = left

    while i <= right and lys[i] <= val:
        if lys[i] == val:
            return i
        i += 1

    return -1


def fibonacci_search(lys, val):
    fibM_minus_2 = 0
    fibM_minus_1 = 1
    fibM = fibM_minus_1 + fibM_minus_2

    while fibM < len(lys):
        fibM_minus_2 = fibM_minus_1
        fibM_minus_1 = fibM
        fibM = fibM_minus_1 + fibM_minus_2

    index = -1

    while fibM > 1:
        i = min(index + fibM_minus_2, len(lys) - 1)

        if lys[i] < val:
            fibM = fibM_minus_1
            fibM_minus_1 = fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
            index = i
        elif lys[i] > val:
            fibM = fibM_minus_2
            fibM_minus_1 = fibM_minus_1 - fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
        else:
            return i

    if fibM_minus_1 and index < len(lys) - 1 and lys[index + 1] == val:
        return index + 1

    return -1


def exponential_search(lys, val):
    if lys[0] == val:
        return 0

    index = 1

    while index < len(lys) and lys[index] <= val:
        index = index * 2

    return BinarySearch(lys[:min(index, len(lys))], val)


def interpolation_search(lys, val):
    low = 0
    high = len(lys) - 1

    while low <= high and val >= lys[low] and val <= lys[high]:
        index = low + \
            int(((float(high - low) /
                (lys[high] - lys[low])) * (val - lys[low])))

        if lys[index] == val:
            return index

        if lys[index] < val:
            low = index + 1
        else:
            high = index - 1

    return -1


arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 1111]
print("Оригинальный массив: ", arr)
start = time.time()
print(f"LinearSearch: {LinearSearch(arr, 20)}")
end = time.time()
print(end - start)
start = time.time()
print(f"BinarySearch: {BinarySearch(arr, 20)}")
end = time.time()
print(end - start)
start = time.time()
print(f"Jump_search: {jump_search(arr, 20)}")
end = time.time()
print(end - start)
start = time.time()
print(f"fibonacci_search: {fibonacci_search(arr, 20)}")
end = time.time()
print(end - start)
start = time.time()
print(f"exponential_search: {exponential_search(arr, 20)}")
end = time.time()
print(end - start)
start = time.time()
print(f"interpolation_search: {interpolation_search(arr, 20)}")
end = time.time()
print(end - start)
