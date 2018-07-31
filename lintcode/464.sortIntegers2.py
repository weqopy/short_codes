class Solution:
    """
    @param A: an integer array
    @return: nothing
    """

    def sortIntegers2(self, A):
        self.quickSort(A, 0, len(A) - 1)

        return A

    def quickSort(self, A, left, right):
        if left > right:
            return
        index = A[left]
        low = left
        high = right

        while left < right:
            while left < right and A[right] >= index:
                right -= 1
            if left < right:
                A[left] = A[right]
                left += 1
            while left < right and A[left] <= index:
                left += 1
            if left < right:
                A[right] = A[left]
                right -= 1

        A[right] = index

        self.quickSort(A, low, left - 1)
        self.quickSort(A, left + 1, high)


A = [3, 2, 1, 4, 5]

r = Solution()
print(r.sortIntegers2(A))
