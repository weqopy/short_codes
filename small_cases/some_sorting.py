# Python 排序算法
arr = [5, 3, 2, 2, 1, 0]

# ---------- quickSort ----------
#


def quickSort(arr, left, right):
    if left > right:
        return
    index = arr[left]
    low = left
    high = right

    while left < right:
        while left < right and arr[right] >= index:
            right -= 1
        if left < right:
            arr[left] = arr[right]
            left += 1
        while left < right and arr[left] <= index:
            left += 1
        if left < right:
            arr[right] = arr[left]
            right -= 1

    arr[right] = index

    quickSort(arr, low, left - 1)
    quickSort(arr, left + 1, high)


quickSort(arr, 0, len(arr) - 1)
print('quickSort: ', arr)

# ---------- another_two_quickSorts ----------
#


def another_quickSort(arr, left, right):
    if left < right:
        # index = partition(arr, left, right)
        index = partition2(arr, left, right)
        another_quickSort(arr, left, index - 1)
        another_quickSort(arr, index + 1, right)


def partition(arr, left, right):
    # while 前后遍历
    index = right
    while left < right:
        if arr[left] <= arr[index]:
            left += 1
        else:
            arr[left], arr[right - 1] = arr[right - 1], arr[left]
            right -= 1
    arr[right], arr[index] = arr[index], arr[right]
    return right


def partition2(arr, left, right):
    # 根据《算法导论》伪代码
    i = left - 1
    for j in range(left, right):
        if arr[j] <= arr[right]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1


another_quickSort(arr, 0, len(arr) - 1)
print('another_quickSort: ', arr)

# ---------- bubbleSort ----------
#


def bubbleSort(arr):
    if len(arr) <= 1:
        return arr
    count = len(arr)
    for i in range(count):
        n = 0
        for j in range(1, count - i):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
                n += 1
        if n == 0:
            break
    return arr


print('bubbleSort: ', bubbleSort(arr))

# ---------- selectSort ----------
#


def selectSort(arr):
    if len(arr) <= 1:
        return arr
    count = len(arr)
    for i in range(count - 1):
        index = i
        for j in range(i + 1, count):
            if arr[index] > arr[j]:
                index = j
        arr[index], arr[i] = arr[i], arr[index]
    return arr


print('selectSort: ', selectSort(arr))

# ---------- insertSort ----------
#


def insertSort(arr):
    if len(arr) <= 1:
        return arr
    count = len(arr)
    for j in range(1, count):
        for i in range(j, 0, -1):
            if arr[i] < arr[i - 1]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
            else:
                break
    return arr


print('insertSort: ', insertSort(arr))

# ---------- shellSort ----------
#


def shellSort(arr):
    if len(arr) <= 1:
        return arr
    count = len(arr)
    gap = count // 2
    while gap > 0:
        for i in range(gap, count):
            temp = arr[i]
            for j in range(i, 0, -gap):
                if temp < arr[j - gap]:
                    arr[j] = arr[j - gap]
                else:
                    j += gap
                    break
            arr[j - gap] = temp
        gap //= 2
    return arr


print('shellSort: ', shellSort(arr))

# ---------- mergeSort ----------
#


def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    index = len(arr) // 2
    L = mergeSort(arr[:index])
    R = mergeSort(arr[index:])
    return merge(L, R)


def merge(L, R):
    i, j = 0, 0
    result = []
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            result.append(L[i])
            i += 1
        else:
            result.append(R[j])
            j += 1
    result += L[i:]
    result += R[j:]
    return result


print('mergeSort: ', mergeSort(arr))

# ---------- heapSort ----------
#


def heapSort(arr):

    # 创建最大堆
    for start in range((len(arr) - 2) // 2, -1, -1):
        sift_down(arr, start, len(arr) - 1)

    # 堆排序
    for end in range(len(arr) - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        sift_down(arr, 0, end - 1)
    return arr


def sift_down(arr, start, end):
    """最大堆调整"""
    root = start
    while True:
        child = 2 * root + 1
        if child > end:
            break
        if child + 1 <= end and arr[child] < arr[child + 1]:
            child += 1
        if arr[root] < arr[child]:
            arr[root], arr[child] = arr[child], arr[root]
            root = child
        else:
            break


print('heapSort: ', heapSort(arr))

# ---------- countingSort ----------
#


def countingSort(arr):
    n = len(arr)
    m = max(arr)
    result = [0] * n
    count = [0] * (m + 1)
    for i in arr:
        count[i] = count[i] + 1
    for j in range(1, m + 1):
        count[j] = count[j] + count[j - 1]

    # 最后一步，逆序循环，保持稳定性
    for k in arr[::-1]:
        result[count[k] - 1] = k
        count[k] = count[k] - 1
    return result


print('countingSort: ', countingSort(arr))
