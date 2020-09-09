# Selection Sort
# https://mp.weixin.qq.com/s/zgDOfXgBB69ySun4nID4-A
“”“
选择排序最简单的版本是不稳定的，比如数组[1,3,2,2]，表示为[1,3,2(a),2(b)]，在经过一轮遍历之后变成了[1,2(b),2(a),3]，
两个2之间的顺序因为第一个2和3的调换而颠倒了，所以不是稳定排序。

不过可以改进一下选择排序变成稳定的。原来不稳定是因为交换位置导致的，现在如果改成插入操作（不是使用数组而是链表，把最大的元素插入到最后）的话，就能变成稳定排序。
比如[1,3,2(a),2(b)]，在第一轮中变成了[1,2(a),2(b),3]，这样就能够保持相对位置，变成稳定排序。
”“”

def selection_sort(arr):
    # selection sort # time O(N^2), space O(1)
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j

        if i != min_idx:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


if __name__ == '__main__':
    arr = [22, 34, 3, 32, 82, 55, 89, 50, 37, 5, 64, 35, 9, 70]
    res = selection_sort(arr)
    print(res)
