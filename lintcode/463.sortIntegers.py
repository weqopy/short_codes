class Solution:
    """
    @param A: an integer array
    @return: nothing
    """

    def sortIntegers(self, A):
        ln = len(A)
        if ln < 2:
            return A

        for i in range(ln - 1):
            for j in range(1, ln):
                if A[j - 1] > A[j]:
                    A[j - 1], A[j] = A[j], A[j - 1]
        return A


r = Solution()
print(r.sortIntegers([3, 2, 1, 4, 5]))
