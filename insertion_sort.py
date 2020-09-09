# Insertion Sort
# space O(1).
# worst time O(N^2)
# average time O(N^2)
# best time O(N)
# left is sorted zone, right is unsorted zone (loop invariant)

# base version
# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         for j in range(i, 0, -1):
#             if arr[j] < arr[j - 1]:
#                 arr[j], arr[j - 1] = arr[j - 1], arr[j]
#             else:
#                 break
#
#     return arr

# upgraded version
# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         tmp = arr[i]
#         idx = i
#         for j in range(i-1, -1, -1):
#             if tmp < arr[j]:
#                 arr[j+1] = arr[j]
#                 idx -= 1
#             else:
#                 break
#         arr[idx] = tmp
#     return arr

def insertion_sort(arr):
    size = len(arr)

    for i in range(1, size):
        tmp = arr[i]
        j = i

        while j > 0 and arr[j - 1] > tmp:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = tmp


    return arr

if __name__ == '__main__':
    arr = [22, 34, 3, 32, 82, 55, 89, 50, 37, 5, 64, 35, 9, 70]
    res = insertion_sort(arr)
    print(res)
