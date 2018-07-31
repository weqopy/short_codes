class Solution:
    def DeleteDigits(self, A, k):
        if len(A) == 0:
            return
        elif k == 0:
            return A

        for i in range(k):
            j = 0
            while len(A) > 0 and A[0] == '0':
                A = A[1:]

            while j < len(A) - 1 and A[j] <= A[j + 1]:
                j += 1
            A = A[:j] + A[j + 1:]

        return A


A = '178542'
k = 4


res = Solution()
print(res.DeleteDigits(A, k))
