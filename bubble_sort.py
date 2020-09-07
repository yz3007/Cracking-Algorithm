# Bubble Sort
# [22, 34, 3, 32, 82, 55, 89, 50, 37, 5, 64, 35, 9, 70]

# https://github.com/hustcc/JS-Sorting-Algorithm/blob/master/1.bubbleSort.md
# def bubbleSort(arr):
#     for i in range(1, len(arr)):
#         for j in range(0, len(arr)-i):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr


# def bubble_sort(arr):
#     for i in range(len(arr)-1, -1, -1):
#         for j in range(i):
#             if arr[j] > arr[j+1]:
#                 arr[j + 1] ^= arr[j]
#                 arr[j] ^= arr[j + 1]
#                 arr[j + 1] ^= arr[j]
#     return arr
"""
time O(N^2), space O(1)

average O(N^2), best O(N): already sorted from small to large,
worst O(N^2): reverse sorted.
稳定性：稳定 （稳定性：排序后 2 个相等键值的顺序和排序之前它们的顺序相同）
"""



# flag mode
def bubble_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        flag = True
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j + 1] ^= arr[j]
                arr[j] ^= arr[j + 1]
                arr[j + 1] ^= arr[j]
                flag = False
        if flag: # stop advance
            return arr
    return arr

if __name__ == '__main__':
    arr = [22, 34, 3, 32, 82, 55, 89, 50, 37, 5, 64, 35, 9, 70]
    res = bubble_sort(arr)
    print(res)
