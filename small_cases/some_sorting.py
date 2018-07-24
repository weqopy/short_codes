# Python 排序算法


arr = [5, 3, 2, 2, 1, 0]


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


quickSort(arr, 0, len(arr)-1)


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


print(bubbleSort(arr))


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


print(selectSort(arr))


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


print(insertSort(arr))


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


print(shellSort(arr))


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


print(mergeSort(arr))


def heap_sort(arr):

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


print(heap_sort(arr))


def countingSort(arr):
    n = len(arr)
    m = max(arr)
    result = [0] * n
    count = [0] * (m + 1)
    for i in arr:
        count[i] = count[i] + 1
    for j in range(1, m + 1):
        count[j] = count[j] + count[j - 1]
    for k in arr:
        result[count[k] - 1] = k
        count[k] = count[k] - 1
    return result


print(countingSort(arr))


# 二叉树


# 二叉树
# 添加子树
# 深度查找 & 广度查找


from queue import Queue


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.lc = None
        self.rc = None

    def insert_left(self, value):
        if self.lc is None:
            self.lc = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.lc = self.lc
            self.lc = new_node

    def insert_right(self, value):
        if self.rc is None:
            self.rc = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.rc = self.rc
            self.rc = new_node

    def pre_order(self):
        print(self.value)

        if self.lc:
            self.lc.pre_order()

        if self.rc:
            self.rc.pre_order()

    def in_order(self):
        if self.lc:
            self.lc.in_order()

        print(self.value)

        if self.rc:
            self.rc.in_order()

    def post_order(self):
        if self.lc:
            self.lc.post_order()

        if self.rc:
            self.rc.post_order()

        print(self.value)

    def bfs(self):
        queue = Queue()
        queue.put(self)

        while not queue.empty():
            current_node = queue.get()
            print(current_node.value)

            if current_node.lc:
                queue.put(current_node.lc)

            if current_node.rc:
                queue.put(current_node.rc)


a_node = BinaryTree('a')
a_node.insert_left('b')
a_node.insert_right('c')

b_node = a_node.lc
b_node.insert_right('d')

c_node = a_node.rc
c_node.insert_left('e')
c_node.insert_right('f')

d_node = b_node.rc
e_node = c_node.lc
f_node = c_node.rc


for i in 'abcdef':
    print(i + '_node: ', eval(i + '_node').value)
print('a_node.pre_order: ')
a_node.pre_order()
print('a_node.in_order: ')
a_node.in_order()
print('a_node.post_order: ')
a_node.post_order()
print('a_node.bfs: ')
a_node.bfs()
