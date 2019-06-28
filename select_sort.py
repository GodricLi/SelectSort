# _*_ coding=utf-8 _*_


# 选择排序，时间复杂度O(n²)
def select_sort(arr):
    """
    首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置。
    再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
    重复第二步，直到所有元素均排序完毕。
    :param arr:
    :return:
    """
    for i in range(len(arr) - 1):
        # 记录最小数的索引，设i为最小数的索引
        min_val = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_val]:
                # 找到更小的数，替换
                min_val = j
        # i不是最小数时，将i和最小数交换
        if i != min_val:
            arr[i], arr[min_val] = arr[min_val], arr[i]


num = [33, 11, 12, 1, 2, 3, 4, 5, 22]
select_sort(num)
print(num)
