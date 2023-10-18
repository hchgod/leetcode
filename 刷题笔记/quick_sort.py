# @Time : 2023/9/11 17:50
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # 选择中间的元素作为枢轴

    left = [x for x in arr if x < pivot]  # 划分出比枢轴小的元素
    middle = [x for x in arr if x == pivot]  # 划分出与枢轴相等的元素
    right = [x for x in arr if x > pivot]  # 划分出比枢轴大的元素
    return quicksort(left) + middle + quicksort(right)  # 递归地对左右两部分进行快速排序，并拼接结果


# 示例
arr = [3, 1, 7, 2, 5, 4, 9, 6, 8]
sorted_arr = quicksort(arr)
print(sorted_arr)